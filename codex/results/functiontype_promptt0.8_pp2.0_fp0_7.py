import types
# Test types.FunctionType is a callable
types.FunctionType('foo', (), {})()

# Test types.LambdaType is a callable
types.LambdaType('foo', (), {})()

# Test types.CodeType is not a callable
try:
    types.CodeType('foo', (), {})()
except TypeError:
    pass
else:
    raise Exception("Expected a TypeError")
