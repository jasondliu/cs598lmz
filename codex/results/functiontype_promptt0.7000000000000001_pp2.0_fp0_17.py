import types
# Test types.FunctionType
assert type(lambda x: x) == types.FunctionType, "lambda"
assert type(lambda x: x) == types.LambdaType, "lambda"
assert type(min) == types.BuiltinFunctionType, "min"
assert type(min) != types.FunctionType, "min"

def f(): pass
assert type(f) == types.FunctionType, "f"

class C:
    def f(): pass

assert type(C.f) == types.FunctionType, "C.f"
assert type(C().f) == types.FunctionType, "C().f"

# Test types.GeneratorType
g = (i for i in range(5))
assert type(g) == types.GeneratorType, "g"

def genf():
    yield 1
    yield 2
    yield 3

g = genf()
assert type(g) == types.GeneratorType, "g"

# Test types.MethodType
g = C().f
assert type(g) == types.MethodType, "g"

# Test type.Un
