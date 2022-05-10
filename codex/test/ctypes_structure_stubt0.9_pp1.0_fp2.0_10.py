import ctypes

class S(ctypes.Structure):
    x = 0
    _fields_ = [
            ("x", ctypes.c_int),
            ("y", ctypes.c_float),
            ("z", ctypes.c_double),
            ("flag", ctypes.c_int),
    ]

    def f(self):
        return self.x + 5

s = S()

# This is the offset that references the function object within the instance (sizeof(S) == 16)
TUPLE_OFFSET = 64

# When we look up 'f', we're looking up what's stored at TUPLE_OFFSET in the instance,
# rather than C:\cygwin\home\Tychod\Projects\py26>python
# Python 2.6.4 (r264:75706, Dec  7 2009, 18:45:15) [MSC v.1500 32 bit (Intel)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# >>> class S:
# ...     def __init__(self, n):
# ...             self.x = n

