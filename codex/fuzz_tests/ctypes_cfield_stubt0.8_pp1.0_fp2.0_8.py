import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class MyInt(int):
    pass

# issue: not calling __new__ on subclass of CField
S1 = S.__new__(S)
S1.x = MyInt(1)
assert S1.x == 1

# OK: creates MyInt instance
S2 = S.__new__(S, x=MyInt(1))
assert isinstance(S2.x, MyInt)
assert S2.x == 1

try:
    S3 = S.__new__(S, x=MyInt(1), y=2)
except TypeError:
    pass
else:
    raise RuntimeError("Didn't raise TypeError")

# issue: doesn't prevent instantiation with wrong number of arguments
try:
    S4 = S.__new__(S, 1)
except TypeError:
    pass
else:
    raise RuntimeError("Didn't raise TypeError")

# OK: gets converted to MyInt instance
# (discarding the result is a bit weird, but it's not wrong)
S5 = S.__new__(S
