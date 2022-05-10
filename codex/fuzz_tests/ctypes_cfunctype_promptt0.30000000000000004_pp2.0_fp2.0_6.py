import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

def func(*args):
    print('func called:', args)

CALLBACK = ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.c_int)

# call a function
_ctypes_test.set_callback(CALLBACK(func))
_ctypes_test.call_callback(1, 2)

# call a class method
class Foo:
    def __init__(self):
        self.callback = CALLBACK(self.func)
    def func(self, a, b):
        print('Foo.func called:', a, b)

foo = Foo()
_ctypes_test.set_callback(foo.callback)
_ctypes_test.call_callback(3, 4)

# call a class static method
class Bar:
    @staticmethod
    def func(a, b):
        print('Bar.func called:', a, b)

_ctypes_test.set_callback(CALLBACK(Bar.func))
_ctypes_test
