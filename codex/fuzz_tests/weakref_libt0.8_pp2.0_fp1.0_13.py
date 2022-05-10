import weakref

##########################################################################

message_types = {
    'UNKNOWN': 0,
    'CONNECTED': 1,
    'DISCONNECTED': 2,
    'STARTED': 3,
    'STOPPED': 4,
    'TICK': 5,
    'TIMER': 6,
    'LOG': 7,
    'TRIGGER': 8,
    'BIND': 9,
    'CALL': 10,
    'EXECUTE': 11,
    'SHUTDOWN': 12,
    'LIBRARY': 13,
    'STATESET': 14,
    'STATEGET': 15,
    'STATE': 16,
    'REQUEST_STATE': 17,
    'SIGNAL': 18,
    'EVENT': 19,
}

##########################################################################

class Bindable(object):
    """
        Bindable object
    """

    def __init__(self, name):
        self._name = name
        self._bind_id = None
        self._bind_owner = None

    def bind(self,
