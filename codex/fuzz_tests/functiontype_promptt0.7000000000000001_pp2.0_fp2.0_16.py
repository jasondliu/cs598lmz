import types
# Test types.FunctionType

def foo():
    pass

print type(foo) == types.FunctionType
print type(foo)
print isinstance(foo, types.FunctionType)
print type(print) == types.BuiltinFunctionType
print type(print)
print isinstance(print, types.BuiltinFunctionType)
print type(int) == types.BuiltinFunctionType
print type(int)
print isinstance(int, types.BuiltinFunctionType)
print type(__builtins__.print) == types.BuiltinFunctionType
print type(__builtins__.print)
print isinstance(__builtins__.print, types.BuiltinFunctionType)
print type(__builtins__.int) == types.BuiltinFunctionType
print type(__builtins__.int)
print isinstance(__builtins__.int, types.BuiltinFunctionType)
