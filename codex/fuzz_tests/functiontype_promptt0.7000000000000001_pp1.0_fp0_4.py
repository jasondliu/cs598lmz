import types
# Test types.FunctionType
if types.FunctionType(lambda: None) is types.FunctionType:
    print('PASSED')
else:
    print('FAILED')
if types.FunctionType is types.FunctionType(lambda: None):
    print('PASSED')
else:
    print('FAILED')

# Test types.BuiltinFunctionType
if types.BuiltinFunctionType(len) is types.BuiltinFunctionType:
    print('PASSED')
else:
    print('FAILED')
if types.BuiltinFunctionType is types.BuiltinFunctionType(len):
    print('PASSED')
else:
    print('FAILED')

# Test types.BuiltinMethodType
if types.BuiltinMethodType(str.split) is types.BuiltinMethodType:
    print('PASSED')
else:
    print('FAILED')
if types.BuiltinMethodType is types.BuiltinMethodType(str.split):
    print('PASSED')
else:
    print('FAILED')

# Test types.MethodType
if types.MethodType(lambda
