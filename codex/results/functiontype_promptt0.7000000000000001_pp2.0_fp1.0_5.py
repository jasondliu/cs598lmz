import types
# Test types.FunctionType
a = lambda x: x + 1
b = range
c = (lambda x: x + 1)

assert type(a) is types.FunctionType
assert type(b) is types.BuiltinFunctionType
assert type(c) is types.FunctionType
# Test types.LambdaType
a = lambda x: x + 1
b = (lambda x: x + 1)

assert type(a) is types.LambdaType
assert type(b) is types.LambdaType
# Test types.GeneratorType
a = (x for x in range(10))
b = (x + 1 for x in range(10))
c = ((x + 1) for x in range(10))
d = ((x + 1) for x in range(10) if x > 5)
e = ((x + 1) for x in range(10) if x > 5 else x)
f = ((x + 1) for x in range(10) if x > 5 else (x + 1))

assert type(a) is types.GeneratorType
assert type(b) is types.Gener
