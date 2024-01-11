import base64
import aiohttp
import json
from microBeesPy.bee import Bee

from microBeesPy.exceptions import MicroBeesException, MicroBeesWrongCredentialsException

class MicroBees :
  token = None
  session = None
  HOST = "https://dev.microbees.com/"
  VERSION = "1_0"
  clientID = None
  clientSecret = None 

  def __init__(self,clientID,clientSecret,session = None):
    self.session  = aiohttp.ClientSession() if session is None  else  session
    self.clientID = clientID
    self.clientSecret = clientSecret
  
  async def login(self, username,password,scope="read write"):
    userpass = (
      self.clientID + ":" + self.clientSecret
    )
    auth = base64.b64encode(userpass.encode()).decode()
    data = {
      "username": username,
      "password": password,
      "scope": scope,
      "grant_type": "password",
    }
    headers = {
      "Content-Type": "application/x-www-form-urlencoded",
      "Authorization": "Basic %s" % auth,
    }
    try:
        resp= await self.session.post(self.HOST+"oauth/token",headers = headers, data = data)
        if resp.status == 200:
          response = await resp.text()
          responseObj =  json.loads(response)
          self.token = responseObj.get('access_token')
          return self.token
        else:
          raise MicroBeesWrongCredentialsException("Your username or password is invalid")
    except Exception as e:
      raise e

  async def getBees(self):
    assert self.token is not None, 'Token must be setted'
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer %s" % self.token,
    }
    try:
      resp=  await self.session.post(self.HOST+"v/"+self.VERSION+"/getMyBees", headers = headers)
      if resp.status == 200:
        response = await resp.text()
        responseObj =  json.loads(response)
        return [Bee.from_dict(y) for y in responseObj.get("data")]
      else :
        raise MicroBeesException("Error "+resp.status)
    except Exception as e:
      raise e

  async def sendCommand(self,actuatorID,relayValue, commandType =6):
    assert self.token is not None, 'Token must be setted'
    headers = {
      "Content-Type": "application/json",
      "Authorization": "Bearer %s" % self.token,
    }
    data = {
      "actuatorID": actuatorID,
      "command_type": commandType,
      "data": {
        "actuatorID": actuatorID,
        "command_type": commandType,
        "relay_value": relayValue,
      }
    }
    try:
      resp = await self.session.post(self.HOST+"v/"+self.VERSION+"/sendCommand", json = data, headers = headers)
      print(await resp.text())
      if resp.status == 200:
        response = await resp.text()
        responseObj =  json.loads(response)
        return responseObj.get('status')==0
      else:
        raise MicroBeesException("Error "+resp.status)
    except Exception as e:
      raise e