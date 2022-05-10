import types
# Test types.FunctionType
def f(x):
    return x + 1

assert type(f) is types.FunctionType
# Test types.BuiltinFunctionType
assert type(abs) is types.BuiltinFunctionType

# Test types.MethodType
class C:
    def foo(self, x):
        return self, x
assert type(C().foo) is types.MethodType

# Test types.LambdaType
l = lambda x: x
assert type(l) is types.LambdaType

# Test types.GeneratorType
def g():
    yield 1
    yield 2
    yield 3
assert type(g()) is types.GeneratorType

# Test types.GeneratorType
def gen():
    yield
assert type(gen()) is types.GeneratorType

# Test types.CodeType
assert type(f.__code__) is types.CodeType

# Test types.FrameType
def bar():
    return type(sys._getframe())
assert bar() is types.FrameType

# Test types.TracebackType
try:
    raise TypeError
except
