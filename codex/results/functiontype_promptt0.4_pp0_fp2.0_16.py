import types
# Test types.FunctionType
try:
    types.FunctionType
except AttributeError:
    print("SKIP")
    raise SystemExit

def f():
    pass

print(types.FunctionType)
print(type(f))
print(isinstance(f, types.FunctionType))
print(isinstance(f, types.BuiltinFunctionType))
print(isinstance(f, types.BuiltinMethodType))
print(isinstance(f, types.LambdaType))
print(isinstance(f, types.GeneratorType))

# Test types.BuiltinFunctionType
try:
    types.BuiltinFunctionType
except AttributeError:
    print("SKIP")
    raise SystemExit

print(types.BuiltinFunctionType)
print(type(print))
print(isinstance(print, types.FunctionType))
print(isinstance(print, types.BuiltinFunctionType))
print(isinstance(print, types.BuiltinMethodType))
print(isinstance(print, types.LambdaType))
print(isinstance(print, types.GeneratorType))

#
