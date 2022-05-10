import ctypes
ctypes.cast(int(0), ctypes.py_object)

#
# Test that type() and ctypes.py_object work side-by-side
#
import ctypes

class Foo(object):
    pass

foo = Foo()

assert type(foo) is Foo
