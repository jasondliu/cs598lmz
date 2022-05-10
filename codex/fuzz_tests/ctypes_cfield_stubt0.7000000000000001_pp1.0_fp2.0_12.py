import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class Value(object):
    pass

class CValue(Value):
    """A C value."""
    _immutable_fields_ = ["ctype", "value"]

    def __init__(self, ctype, value):
        self.ctype = ctype
        self.value = value

    def __repr__(self):
        return "<CValue %r>" % (self.value,)

class CArray(Value):
    """A C array."""
    _immutable_fields_ = ["ctype", "items"]

    def __init__(self, ctype, items):
        self.ctype = ctype
        self.items = items

    def __repr__(self):
        return "<CArray %r>" % (self.items,)

class CStruct(Value):
    """A C struct."""
    _immutable_fields_ = ["ctype", "items"]

    def __init__(self, ctype, items):
        self.ctype = ctype
        self.items = items

    def __repr__(self
