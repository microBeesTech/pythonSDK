Official microBees Python Library
===============================

Used as a wrapper dependency in the Home Assistant integration.

Version
-------

0.0.1

Installation
------------

    $ pip3 install microbees

Getting Started
---------------
Go to https://developers.microbees.com/dashboard/ and register your developer App.
Use CLIENTID and CLIENT SECRET generated.

### Actuators
An actuator instance holds the actuator id, name, type, serialnumber, current state
```python
sl = smappee.service_locations.get(1) # where 12345 should be the correct service location id
for actuator_id, actuator in sl.actuators.items():
    actuator.id
    actuator.name
    actuator.type
    actuator.serialnumber
    actuator.state
    actuator.state_options
    actuator.consumption_today
```

Changing the actuator state can be done with the `set_actuator_state` in the `service_location` class.
```python
# Example: turn OFF actuator with id 1 from service location 12345
sl = smappee.service_locations.get(12345) # where 12345 should be the correct service location id
sl.set_actuator_state(id=1, state='OFF')
```

### Sensors
A sensor instance holds the sensor id, name, channels, temperature, humidity and battery level.
```python
sl = smappee.service_locations.get(12345) # where 12345 should be the correct service location id
for sensor_id, sensor in sl.sensors.items():
    sensor.id
    sensor.name
    sensor.channels
    sensor.temperature
    sensor.humidity
    sensor.battery
```

Support
-------
If you find a bug, have any questions about how to use this SDK or have suggestions for improvements then feel free to
file an issue on the GitHub project page [https://github.com/microBeesTech/pythonHASS](https://github.com/microBeesTech/pythonHASS).

License
-------
(MIT License)
