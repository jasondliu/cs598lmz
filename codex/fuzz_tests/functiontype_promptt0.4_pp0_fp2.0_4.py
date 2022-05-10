import types
# Test types.FunctionType
def f(x, y):
    return x + y

assert type(f) == types.FunctionType

# Test types.LambdaType
g = lambda x, y: x + y
assert type(g) == types.LambdaType

# Test types.GeneratorType
def h():
    yield 1
    yield 2
    yield 3

assert type(h()) == types.GeneratorType

# Test types.BuiltinFunctionType
assert type(len) == types.BuiltinFunctionType

# Test types.BuiltinMethodType
assert type([].append) == types.BuiltinMethodType

# Test types.MethodType
class A:
    def m(self):
        pass

a = A()
assert type(a.m) == types.MethodType

# Test types.UnboundMethodType
assert type(A.m) == types.UnboundMethodType

# Test types.TracebackType
try:
    1/0
except Exception as e:
    assert type(e.__traceback__) == types.TracebackType

