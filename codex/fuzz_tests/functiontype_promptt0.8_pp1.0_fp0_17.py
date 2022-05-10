import types
# Test types.FunctionType, types.LambdaType and types.MethodType for
# _instancecheck_ and _subclasscheck_.

# Function
def f(x): pass
assert isinstance(f, types.FunctionType)
assert issubclass(types.FunctionType, types.FunctionType)

# Lambda
l = lambda x:x
assert isinstance(l, types.LambdaType)
assert issubclass(types.LambdaType, types.LambdaType)
assert not issubclass(types.LambdaType, types.FunctionType)

# Method
class A(object):
    def m(self, x): pass

a = A()
m = a.m
assert isinstance(m, types.MethodType)
assert issubclass(types.MethodType, types.MethodType)
assert not issubclass(types.MethodType, types.FunctionType)
assert not issubclass(types.MethodType, types.LambdaType)
