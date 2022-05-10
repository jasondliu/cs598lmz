import types
# Test types.FunctionType
try:
    Class(types.FunctionType)
except TypeError:
    pass
else:
    print('FAILED: function type should be disallowed')
# Test types.BuiltinFunctionType
try:
    Class(types.BuiltinFunctionType)
except TypeError:
    pass
else:
    print('FAILED: builtin function type should be disallowed')
# Test types.UnboundMethodT
