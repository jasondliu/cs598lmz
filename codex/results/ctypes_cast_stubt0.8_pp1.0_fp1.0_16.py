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
assert type(ctypes.py_object(foo)) is Foo

assert type(foo) is not int
assert type(ctypes.py_object(foo)) is not int

#
# Test that types are callable when they have a __call__ method
#
import ctypes

class Foo(object):
    def __call__(self):
        pass

foo = Foo()

assert callable(foo)
assert callable(ctypes.py_object(foo))
