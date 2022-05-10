import types
# Test types.FunctionType
def func(x):
  return x

assert isinstance(func, types.FunctionType)
assert isinstance(func, types.BuiltinFunctionType)
assert isinstance(func, types.BuiltinMethodType)
assert isinstance(func, types.MethodType)

# Test types.MethodType
class A(object):
  def func(self, x):
    return x

assert isinstance(A.func, types.FunctionType)
assert not isinstance(A.func, types.BuiltinFunctionType)
assert not isinstance(A.func, types.BuiltinMethodType)
assert isinstance(A.func, types.MethodType)

assert isinstance(A().func, types.FunctionType)
assert not isinstance(A().func, types.BuiltinFunctionType)
assert not isinstance(A().func, types.BuiltinMethodType)
assert isinstance(A().func, types.MethodType)

# Test types.BuiltinFunctionType
assert isinstance(len, types.FunctionType)
assert isinstance(len, types.BuiltinFunctionType)
assert not
