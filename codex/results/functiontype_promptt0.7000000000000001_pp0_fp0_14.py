import types
# Test types.FunctionType
try:
    x = types.FunctionType
except Exception as e:
    print(type(e))
    print(e.args)
    print(e)

# Test types.LambdaType
try:
    x = types.LambdaType
except Exception as e:
    print(type(e))
    print(e.args)
    print(e)

# Test types.GeneratorType
try:
    x = types.GeneratorType
except Exception as e:
    print(type(e))
    print(e.args)
    print(e)

# Test types.BuiltinFunctionType
try:
    x = types.BuiltinFunctionType
except Exception as e:
    print(type(e))
    print(e.args)
    print(e)

# Test types.BuiltinMethodType
try:
    x = types.BuiltinMethodType
except Exception as e:
    print(type(e))
    print(e.args)
    print(e)

# Test types.MethodType
try:
    x
