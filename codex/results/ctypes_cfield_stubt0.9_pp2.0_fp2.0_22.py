import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

field = ctypes.CField(1, S.x, (1,))

assert field.offset == 1
assert field.size == 4
assert field.index == (1,)
assert field.name == "x"
try:
    field.pack_for_hash(1234)
except AttributeError: pass
else:
    raise AssertionError
print("if this is the only output we're ok")
