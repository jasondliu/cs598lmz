import ctypes
ctypes.cast(p, ctypes.c_void_p).value

# We can write this more compactly using operator.methodcaller:
from operator import methodcaller
methodcaller('value', p)()

# We can also build a wrapper class that encapsulates this logic:
class Vvoidptr(object):
    def __init__(self, obj):
        self.obj = obj

    def __call__(self):
        return ctypes.cast(self.obj, ctypes.c_void_p).value

vvoidptr = Vvoidptr(p)
vvoidptr()
