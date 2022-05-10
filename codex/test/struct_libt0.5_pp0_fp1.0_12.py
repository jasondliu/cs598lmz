import _struct

from . import _util

_struct_I = _struct.Struct('!I')

class _Message(object):
    def __init__(self, msg_type, msg_data):
        self.msg_type = msg_type
        self.msg_data = msg_data

    def to_bytes(self):
        return _struct_I.pack(self.msg_type) + self.msg_data

class _MessageType(object):
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, self.name)

    def __eq__(self, other):
        if not isinstance(other, _MessageType):
            return NotImplemented
        return self.value == other.value

