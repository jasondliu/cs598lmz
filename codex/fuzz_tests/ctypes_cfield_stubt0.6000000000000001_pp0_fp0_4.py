import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

assert isinstance(S.x, ctypes.CField)
assert S.x.__name__ == "x"
assert type(S.x.size) is int
assert type(S.x.offset) is int
assert isinstance(S.x.type, type)
assert S.x.index == 0
assert S.x.pack == 1

try:
    S.x.unknown
except AttributeError:
    pass
else:
    raise Exception("should have raised AttributeError")

assert repr(S.x) == "<Field type=c_int, ofs=0, size=4>"

# test a bitfield

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int, 3)]
assert S.x.__name__ == "x"
assert S.x.size == 32
assert S.x.offset == 0
assert S.x.type is ctypes.c_int
assert S.x.index == 0
assert S.x.pack == 1
assert S.x.bitsize ==
