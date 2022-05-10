import types
# Test types.FunctionType
def f(a):
    return a
x = f(1)
assert type(x) == type(f) == types.FunctionType
# Test types.LambdaType
g = lambda a: a
x = g(1)
assert type(x) == type(g) == types.LambdaType
# Test types.GeneratorType
def h(a):
    yield a
x = h(1)
assert type(x) == type(h) == types.GeneratorType
# Test types.MethodType
class A:
    pass
a = A()
a.f = f
assert type(a.f) == types.MethodType
a.g = g
assert type(a.g) == types.MethodType
a.h = h
assert type(a.h) == types.MethodType

# Test for __module__ attribute on functions when the function does not have a
# source filename attribute.
import types
def f(): pass
assert f.__module__ == "__main__"
assert type(f).__module__ == "__main__"

#
