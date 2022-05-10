import types
# Test types.FunctionType

def f1(x):
    return x + 1

class C:
    def __call__(self, x):
        return x + 1

x = C()

assert isinstance(f1, types.FunctionType)
assert not isinstance(x, types.FunctionType)

# Test types.LambdaType

f2 = lambda: 1

assert isinstance(f2, types.LambdaType)
assert not isinstance(f1, types.LambdaType)

# Test types.GeneratorType

def f3():
    yield 1

g = f3()

assert isinstance(g, types.GeneratorType)
assert not isinstance(f3, types.GeneratorType)

# Test types.BuiltinFunctionType

assert isinstance(len, types.BuiltinFunctionType)
assert not isinstance(f1, types.BuiltinFunctionType)

# Test types.BuiltinMethodType

assert isinstance(len, types.BuiltinMethodType)
assert not isinstance(f1, types.BuiltinMethodType
