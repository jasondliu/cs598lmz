import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42
assert fun() == 42

# Make sure the class is still working
@functools.total_ordering
class Foo(object):
    def __init__(self, value):
        self.value = value
    def __eq__(self, other):
        return self.value == other.value
    def __lt__(self, other):
        return self.value < other.value

assert Foo(1) <= Foo(2)
assert Foo(3) == Foo(3)
assert Foo(4) >= Foo(3)
assert not Foo(5) != Foo(5)

@functools.lru_cache(maxsize=128, typed=True)
def fib(n):
    if n < 2:
        return n
    return fib(n-2) + fib(n-1)

assert fib(120) == 5_358_709_116_749

# NOTE: Only test if the C version is used, because the version in CPython
# doesn't accept keyword arguments.
if hasattr(partialmethod, '__module__'):

