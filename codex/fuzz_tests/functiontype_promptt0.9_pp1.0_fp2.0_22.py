import types
# Test types.FunctionType function
y = lambda x: x + 1
if types.FunctionType(y.func_code, y.func_globals, "y", y.func_defaults, y.func_closure) is not y:
    raise TypeError
