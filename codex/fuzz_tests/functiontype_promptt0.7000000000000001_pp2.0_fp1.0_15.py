import types
# Test types.FunctionType
assert isinstance(test, types.FunctionType)

# Test types.InstanceType
assert isinstance(test(), types.InstanceType)

# Test types.LambdaType
assert isinstance(lambda x: x, types.LambdaType)

# Test types.MethodType
# Bug: https://bitbucket.org/pypy/pypy/issue/1882/methodtype-is-not-watched-by-isinstance
assert isinstance(test, types.MethodType)
