import ctypes
# Test ctypes.CField.__get__()

class MyLong(ctypes.c_long):
    _fields_ = [("one", ctypes.c_long),
                ("two", ctypes.c_long),
                ("three", ctypes.c_long)]
    def __init__(self, value=0L):
        super(MyLong, self).__init__(value)

o = MyLong(0x01020304)
o.one

# Issue #2869, ctypes.c_void_p.__getattr__

class TestGetattr:
    def __init__(self):
        self.__dict__["_name"] = "foo"

t = TestGetattr()
ctypes.c_void_p(t)

# Issue #2870, ValueError exception raised instead of IndexError

try:
    ctypes.create_string_buffer("abc", 2)
except ValueError:
    pass
else:
    raise RuntimeError("failed")

# Issue #2872, calling a function with a pointer to the same instance
# as the argument causes the
