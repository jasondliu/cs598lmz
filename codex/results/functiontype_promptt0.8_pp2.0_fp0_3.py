import types
# Test types.FunctionType


def foo():
    pass


def foo2(a):
    pass


def foo3(a, b):
    pass


def foo4(a=42):
    pass


def foo5(a=42, b=43):
    pass


def foo6(a, b=43):
    pass


def foo7(a=42, b):
    pass


f = types.FunctionType(foo.__code__, {}, "foo")
assert f() is None

f = types.FunctionType(foo2.__code__, {}, "foo2")
try:
    f()
except TypeError:
    pass
else:
    raise AssertionError("should have raised TypeError")

f = types.FunctionType(foo3.__code__, {}, "foo3")
try:
    f()
except TypeError:
    pass
else:
    raise AssertionError("should have raised TypeError")

f = types.FunctionType(foo4.__code__, {}, "foo4")
assert f() == 42

