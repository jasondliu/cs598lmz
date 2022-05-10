import types
# Test types.FunctionType
def f(): pass
f1 = types.FunctionType(f.__code__, f.__globals__, argdefs=f.__defaults__)
assert f1.__name__ == "f"
assert f1() == None

def f(a, b, c): return a + b + c
f2 = types.FunctionType(f.__code__, f.__globals__, argdefs=f.__defaults__)
assert f2.__name__ == "f"
assert f2(1, 2, 3) == 6

# Test types.GeneratorType
def generator():
    yield 1
    yield 2
    yield 3

g = generator()
assert isinstance(g, types.GeneratorType)

# Test types.BuiltinFunctionType
assert isinstance(abs, types.BuiltinFunctionType)

# Test types.BuiltinMethodType
assert isinstance(abs, types.BuiltinMethodType)

# Test types.LambdaType
l = types.LambdaType(lambda x: x, globals(), "
