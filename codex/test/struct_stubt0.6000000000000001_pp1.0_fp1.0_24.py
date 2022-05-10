from _struct import Struct
s = Struct.__new__(Struct)
s_format = 'ci'
s.format = s_format
s.size = s.calcsize(s_format)

def pack(s, *args, **kwargs):
    return s.pack(*args, **kwargs)

def unpack(s, *args, **kwargs):
    return s.unpack(*args, **kwargs)

def calcsize(s, *args, **kwargs):
    return s.calcsize(*args, **kwargs)

class unpack_from(object):
    __qualname__ = 'unpack_from'

    def __init__(self, s):
        self.s = s

    def __call__(self, *args, **kwargs):
        return self.s.unpack_from(*args, **kwargs)

unpack_from = unpack_from(s)
