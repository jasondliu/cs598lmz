import types
# Test types.FunctionType
def test():
    pass
assert isinstance(test, types.FunctionType)
assert isinstance(test, types.BuiltinFunctionType)

# Test types.LambdaType
test = lambda : None
assert isinstance(test, types.LambdaType)
assert isinstance(test, types.FunctionType)

# Test types.BuiltinFunctionType
test = abs
assert isinstance(test, types.BuiltinFunctionType)
assert isinstance(test, types.FunctionType)

# Test types.GeneratorType
def test():
    yield 101
assert isinstance(test, types.GeneratorType)
assert isinstance(test(), types.GeneratorType)

# Test types.ClassType: __class__ is normally set, this only happens if __class__ set specially
class Test:
    pass
assert isinstance(Test, types.ClassType)
assert isinstance(Test(), types.ClassType)

# Test types.TypeType:
assert isinstance(int, types.TypeType)
assert isinstance("test", types.TypeType)
assert isinstance(Test, types
