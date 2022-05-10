import types
# Test types.FunctionType
def f():
    pass

print type(f) == types.FunctionType
print type(lambda: None) == types.FunctionType
print type(int) == types.FunctionType

# Test types.LambdaType
print type(lambda: None) == types.LambdaType
print type(f) == types.LambdaType
print type(int) == types.LambdaType

# Test types.GeneratorType
def g():
    yield 1

print type(g()) == types.GeneratorType

# Test types.BuiltinFunctionType
print type(int) == types.BuiltinFunctionType
print type(f) == types.BuiltinFunctionType
print type(lambda: None) == types.BuiltinFunctionType

# Test types.BuiltinMethodType
print type(int.__add__) == types.BuiltinMethodType
print type(f.__call__) == types.BuiltinMethodType
print type(lambda: None).__call__ == types.BuiltinMethodType

# Test types.MethodType
class C(object):
    def m
