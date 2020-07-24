class MicroBeesSensor:

    def __init__(self, id, name, value):
        # configuration details
        self._id = id
        self._name = name
        self._value = value

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value
