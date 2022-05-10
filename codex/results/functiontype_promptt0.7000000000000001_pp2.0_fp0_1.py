import types
# Test types.FunctionType is implemented in builtins.
assert issubclass(types.FunctionType, types.BuiltinFunctionType)

# Test that the old __new__ still exists (probably not necessary).
assert types.FunctionType.__new__ is object.__new__
# Test that the old __init__ still exists (probably not necessary).
assert types.FunctionType.__init__ is object.__init__

# Test that the __init__ implementation can be called.
assert isinstance(types.FunctionType(lambda x: x, {}), types.FunctionType)

# Test that calling the new __new__ directly works.
assert isinstance(types.FunctionType.__new__(types.FunctionType,
                                             lambda x: x, {}),
                  types.FunctionType)

# Test that the class isn't broken.
assert isinstance(types.FunctionType(lambda x: x, {}), types.FunctionType)

# Test that calling the new __new__ directly works.
assert isinstance(types.FunctionType.__new__(types.FunctionType,
                                             lambda x: x, {}),
                 
