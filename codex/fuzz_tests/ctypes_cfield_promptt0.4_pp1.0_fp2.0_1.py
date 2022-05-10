import ctypes
# Test ctypes.CField.from_param

class S(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int)]

class C(ctypes.Structure):
    _fields_ = [("s", S)]

s = S(42)
c = C(s)

assert c.s.x == 42

# The following test checks that the ctypes.CField.from_param() method
# is called when a structure field is passed to a function.

# The from_param() method of the ctypes.CField class is called
# when a structure field is passed to a function.

# The from_param() method of the ctypes.CField class is called
# when a structure field is passed to a function.

# The from_param() method of the ctypes.CField class is called
# when a structure field is passed to a function.

# The from_param() method of the ctypes.CField class is called
# when a structure field is passed to a function.

# The from_param() method of the ctypes.CField class is
