import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    _fields_ = [('x', x)]

S()
S(x=1)
S(*[1])
S(**{'x': 1})
S(1)
S((1,))
S([1])
S({'x': 1})
S(**{})
S(*[])
S(x=1, y=2)
S(x=1, **{})
S(**{'x': 1}, y=2)
S(x=1, **{'x': 2})
S(x=1, **{'y': 2})
S(x=1, **{'y': 2}, y=3)
S(**{'x': 1}, **{'y': 2})

# This should fail
try:
    S(x=1, **{'x': 2}, **{'y': 3})
except TypeError:
    pass

# This should fail
try:
    S(**{'x': 1}, **{'y': 2}, x=3)
except TypeError:
   
