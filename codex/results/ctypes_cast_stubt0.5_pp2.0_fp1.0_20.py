import ctypes
ctypes.cast(0, ctypes.py_object)

class Foo(object):
    pass

Foo()

# Control should not reach here
assert False
