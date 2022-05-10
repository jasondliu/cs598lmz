import types
# Test types.FunctionType
def f(x):
    return x + 1

assert type(f) == types.FunctionType
assert type(lambda x: x + 1) == types.FunctionType

# Test types.BuiltinFunctionType
assert type(abs) == types.BuiltinFunctionType
assert type(len) == types.BuiltinFunctionType
assert type(list) == types.BuiltinFunctionType

# Test types.BuiltinMethodType
assert type(list.append) == types.BuiltinMethodType
assert type(list.insert) == types.BuiltinMethodType

# Test types.LambdaType
assert type(lambda x: x + 1) == types.LambdaType

# Test types.GeneratorType
def g():
    yield 1
    yield 2

assert type(g()) == types.GeneratorType

# Test types.MethodType
class C:
    def f(self):
        return 1

assert type(C().f) == types.MethodType

# Test types.UnboundMethodType
assert type(C.f) == types.UnboundMethodType


