import types
# Test types.FunctionType
def f(): pass
assert type(f) is types.FunctionType
assert isinstance(f, types.FunctionType)
def g(func):
    assert type(func) is types.FunctionType
g(f)

# Test types.BuiltinFunctionType
assert type(len) is types.BuiltinFunctionType
assert isinstance(len, types.BuiltinFunctionType)

# Test types.LambdaType
assert type(lambda : None) is types.LambdaType
assert isinstance(lambda : None, types.LambdaType)

# Test types.ClassType
class A: pass
assert type(A) is types.ClassType
assert isinstance(A, types.ClassType)
assert type(A()) is types.ClassType
assert isinstance(A(), types.ClassType)
A = type('A', (), {})
assert type(A) is type
assert isinstance(A, type)
assert type(A()) is A
assert isinstance(A(), A)

# Test types.TypeType
assert type(type) is types.TypeType
assert isinstance
