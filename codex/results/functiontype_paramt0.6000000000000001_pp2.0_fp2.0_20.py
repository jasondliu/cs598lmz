from types import FunctionType
list(FunctionType(f.__code__, globals(), "foo"))

# fmt: off
def f():
    yield 1
    yield 2
    yield 3
# fmt: on

bytes(f())
