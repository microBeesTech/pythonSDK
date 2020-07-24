import requests
import datetime as dt
import functools
from .config import config
from .helper import urljoin
from requests.exceptions import HTTPError, ConnectTimeout
from requests_oauthlib import OAuth2Session
import pytz
import numbers


def authenticated(func):
    # Decorator to refresh expired access tokens
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        self = args[0]
        try:
            return func(*args, **kwargs)
        except HTTPError as e:
            if e.response.status_code == 401:
                self._oauth.token = self.refresh_tokens()
            return func(*args, **kwargs)
    return wrapper


class MicroBeesApi(object):

    def __init__(
            self,
            client_id,
            client_secret,
            redirect_uri=None,
            token=None,
            token_updater=None,
    ):
        self._client_id = client_id
        self._client_secret = client_secret
        self._token_updater = token_updater

        extra = {"client_id": self._client_id, "client_secret": self._client_secret}

        self._oauth = OAuth2Session(
            client_id=client_id,
            token=token,
            redirect_uri=redirect_uri,
            token_updater=token_updater,
        )


    @property
    def headers(self):
        return {"Authorization": f"Bearer {self._oauth.access_token}"}


    @authenticated
    def get_metering_configuration(self, service_location_id):
        url = urljoin(config['API_URL'][self._farm]['servicelocation_url'], service_location_id, "meteringconfiguration")
        r = requests.get(url, headers=self.headers)
        r.raise_for_status()
        return r.json()



    def _to_milliseconds(self, time):
        if isinstance(time, dt.datetime):
            if time.tzinfo is None:
                time = time.replace(tzinfo=pytz.UTC)
            return int(time.timestamp() * 1e3)
        elif isinstance(time, numbers.Number):
            return time
        else:
            raise NotImplementedError("Time format not supported. Use milliseconds since epoch,\
                                        Datetime or Pandas Datetime")

    def get_authorization_url(self, state):
        return self._oauth.authorization_url(config['API_URL'][self._farm]['authorize_url'], state)

    def request_token(self, authorization_response, code):
        return self._oauth.fetch_token(
            token_url=config['API_URL'][self._farm]['token_url'],
            authorization_response=authorization_response,
            code=code,
            client_secret=self.client_secret,
        )

    def refresh_tokens(self):
        token = self._oauth.refresh_token(token_url=config['API_URL'][self._farm]['token_url'])

        if self.token_updater is not None:
            self.token_updater(token)

        return token
