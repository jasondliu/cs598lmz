import types
# Test types.FunctionType
def testFunctionType():
    def f(): pass
    assert type(f) is types.FunctionType
    assert type(testFunctionType) is types.FunctionType
    assert type(int) is not types.FunctionType
testFunctionType()

# Test types.BuiltinFunctionType
def testBuiltinFunctionType():
    import __builtin__
    assert type(__builtin__.id) is types.BuiltinFunctionType
    assert type(__builtin__.len) is types.BuiltinFunctionType
    assert type(__builtin__.int) is types.BuiltinFunctionType
    assert type(__builtin__.enumerate) is types.BuiltinFunctionType
    assert type(__builtin__.open) is types.BuiltinFunctionType
    assert type(__builtin__.min) is types.BuiltinFunctionType
    assert type(__builtin__.sorted) is types.BuiltinFunctionType
testBuiltinFunctionType()

# Test types.ClassType
def testClassType():
    assert type(Exception) is not types.ClassType
    assert type
