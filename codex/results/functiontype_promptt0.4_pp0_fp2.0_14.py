import types
# Test types.FunctionType and types.LambdaType

class A:
    def f(self): pass
    g = lambda x: x

a = A()

print type(A.f)
print type(a.f)
print type(a.g)

assert isinstance(A.f, types.FunctionType)
assert isinstance(a.f, types.FunctionType)
assert isinstance(a.g, types.LambdaType)

assert not isinstance(A.f, types.LambdaType)
assert not isinstance(a.f, types.LambdaType)
assert not isinstance(a.g, types.FunctionType)

print type(A.f) is types.FunctionType
print type(a.f) is types.FunctionType
print type(a.g) is types.LambdaType

print type(A.f) == types.FunctionType
print type(a.f) == types.FunctionType
print type(a.g) == types.LambdaType

assert type(A.f) is not types.LambdaType
