import types
# Test types.FunctionType
class C(types.FunctionType):
    pass

def f(x):
    return x

g = C(f.__code__, {}, f.__name__, f.__defaults__, f.__closure__)
assert g(3) == 3

# Test types.BuiltinFunctionType
def f1(x):
    return x

g1 = types.BuiltinFunctionType(f1, {}, f1.__name__, f1.__defaults__, f1.__closure__)
assert g1(3) == 3

# Test types.MethodType
class C:
    def f(self, x):
        return x

c = C()
g = types.MethodType(c.f, c)
assert g(3) == 3

# Test types.ModuleType
m = types.ModuleType("foo")
assert m.__name__ == "foo"

# Test types.TracebackType
import sys
import inspect
def g():
    1/0

try:
    g()
except ZeroDivisionError:
