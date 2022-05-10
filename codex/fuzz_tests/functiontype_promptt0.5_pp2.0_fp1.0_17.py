import types
# Test types.FunctionType

def func(x):
    return x

assert type(func) == types.FunctionType
assert type(func) is types.FunctionType
assert isinstance(func, types.FunctionType)
assert isinstance(func, types.FunctionType)
assert issubclass(types.FunctionType, object)
assert issubclass(types.FunctionType, object)

# Test types.BuiltinFunctionType

import math

assert type(math.fsum) == types.BuiltinFunctionType
assert type(math.fsum) is types.BuiltinFunctionType
assert isinstance(math.fsum, types.BuiltinFunctionType)
assert isinstance(math.fsum, types.BuiltinFunctionType)
assert issubclass(types.BuiltinFunctionType, object)
assert issubclass(types.BuiltinFunctionType, object)

# Test types.MethodType

class A:
    def meth(self):
        return self

a = A()
assert type(a.meth) == types.MethodType
assert type(a.meth) is types.MethodType
assert
