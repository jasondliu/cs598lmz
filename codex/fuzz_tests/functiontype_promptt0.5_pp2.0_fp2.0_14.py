import types
# Test types.FunctionType
try:
    types.FunctionType
except AttributeError:
    pass
else:
    raise TestFailed("types.FunctionType shouldn't exist")

# Test types.BuiltinFunctionType
try:
    types.BuiltinFunctionType
except AttributeError:
    pass
else:
    raise TestFailed("types.BuiltinFunctionType shouldn't exist")

# Test types.MethodType
try:
    types.MethodType
except AttributeError:
    pass
else:
    raise TestFailed("types.MethodType shouldn't exist")

# Test types.BuiltinMethodType
try:
    types.BuiltinMethodType
except AttributeError:
    pass
else:
    raise TestFailed("types.BuiltinMethodType shouldn't exist")

# Test types.ClassType
try:
    types.ClassType
except AttributeError:
    pass
else:
    raise TestFailed("types.ClassType shouldn't exist")

# Test types.UnboundMethodType
try:
    types.UnboundMethodType
except AttributeError:
    pass

