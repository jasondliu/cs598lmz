import types
# Test types.FunctionType
def func(a):
    return a
assert type(func) == types.FunctionType

# Test types.LambdaType
lam = lambda x: x
assert type(lam) == types.LambdaType

# Test types.GeneratorType
def gen():
    yield 1
g = gen()
assert type(g) == types.GeneratorType

# Test types.CodeType
assert type(func.__code__) == types.CodeType
assert type(lam.__code__) == types.CodeType
assert type(gen.__code__) == types.CodeType

# Test types.BuiltinFunctionType
assert type(abs) == types.BuiltinFunctionType

# Test types.BuiltinMethodType
assert type([].append) == types.BuiltinMethodType

# Test types.ModuleType
assert type(types) == types.ModuleType

# Test types.UnboundMethodType
class A:
    def f(self):
        pass
assert type(A.f) == types.UnboundMethodType

# Test types.MethodType
a = A
