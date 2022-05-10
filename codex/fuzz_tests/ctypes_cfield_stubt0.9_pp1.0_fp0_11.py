import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

# test CField.from_address
s = S()
assert S.x.from_address(id(s)).value == 0

# test CField.to_address
s = S(1)
assert ctypes.addressof(s) == S.x.__get__(s, S).to_address()

# test CField.size
assert ctypes.sizeof(s.x) == S.x.size
