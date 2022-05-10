import _struct
import sys

PY3 = sys.version_info[0] == 3

if PY3:
    def string_at(addr, size=-1):
        data = _ctypes_test.string_at(addr, size)
        if size < 0:
            size = len(data)
        return data.decode('latin1')
else:
    def string_at(addr, size=-1):
        return _ctypes_test.string_at(addr, size)

def sizeof(typ):
    if type(typ) is not type:
        raise TypeError("sizeof() argument should be type, not %s" % type(typ))
    return _ctypes.sizeof(typ._type_)

def byref(obj, offset=0):
    return _ctypes.byref(obj, offset)

def alignment(typ):
    return _ctypes.alignment(typ._type_)

def addressof(obj):
    return _ctypes.addressof(obj)

