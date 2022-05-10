import types
# Test types.FunctionType
def func():
    pass

x = func

print('func', type(func))
print('x', type(x))
print('x.__class__', x.__class__)
print('types.FunctionType', types.FunctionType)
print('isinstance(x, types.FunctionType)', isinstance(x, types.FunctionType))
print('isinstance(x, types.BuiltinFunctionType)', isinstance(x, types.BuiltinFunctionType))

# Test types.BuiltinFunctionType
print('isinstance(len, types.BuiltinFunctionType)', isinstance(len, types.BuiltinFunctionType))

# Test types.BuiltinMethodType
print('isinstance(x.__class__, types.BuiltinMethodType)', isinstance(x.__class__, types.BuiltinMethodType))

# Test types.MethodType
def func2(self):
    pass

class A(object):
    pass

A.method = func2
x = A()
print('isinstance(x.method, types.MethodType)', isinstance(
