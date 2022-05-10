import types
# Test types.FunctionType
if not isinstance(types.FunctionType, types.TypeType):
    print("SKIP")
    raise SystemExit

# Test types.BuiltinFunctionType
if not isinstance(len, types.BuiltinFunctionType):
    print("SKIP")
    raise SystemExit

# Test types.MethodType
if not isinstance("".find, types.MethodType):
    print("SKIP")
    raise SystemExit

# Test types.UnboundMethodType
if not isinstance(str.find, types.UnboundMethodType):
    print("SKIP")
    raise SystemExit

# Test types.BuiltinMethodType
if not isinstance("".find, types.BuiltinMethodType):
    print("SKIP")
    raise SystemExit

# Test types.LambdaType
if not isinstance(lambda: None, types.LambdaType):
    print("SKIP")
    raise SystemExit

# Test types.GeneratorType
if not isinstance((x for x in range(10)), types.GeneratorType):
    print("SKIP")
    raise System
