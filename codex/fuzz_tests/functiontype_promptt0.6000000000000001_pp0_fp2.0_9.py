import types
# Test types.FunctionType
def f():
    pass
if type(f) != types.FunctionType:
    print('FAILED: not a function type')
if type(f) == types.BuiltinFunctionType:
    print('FAILED: is a builtin function type')

# Test types.BuiltinFunctionType
def g():
    pass
if type(g) != types.FunctionType:
    print('FAILED: not a function type')
if type(g) != types.BuiltinFunctionType:
    print('FAILED: not a builtin function type')
