import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

class MyClass:
    def __init__(self):
        self.my_callback = FUNTYPE(self.my_callback)

    def my_callback(self, a, b):
        return a + b

obj = MyClass()

# This works
obj.my_callback(1, 2)

# This doesn't
obj.my_callback(ctypes.c_int(1), ctypes.c_int(2))
</code>
The error is:
<code>TypeError: an integer is required
</code>
I'm trying to use this in a Cython module, but I'm not sure if the problem is with Cython or with ctypes.

