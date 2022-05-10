import types
# Test types.FunctionType
def test_types_FunctionType():
    assert isinstance(test_types_FunctionType, types.FunctionType)

# Test types.GeneratorType
def test_types_GeneratorType():
    def gen():
        yield 1
    assert isinstance(gen(), types.GeneratorType)

# Test types.LambdaType
def test_types_LambdaType():
    assert isinstance(lambda: 0, types.LambdaType)

# Test types.MethodType
def test_types_MethodType():
    class A:
        def meth(self):
            pass
    assert isinstance(A().meth, types.MethodType)

# Test types.ModuleType
def test_types_ModuleType():
    assert isinstance(types, types.ModuleType)

# Test types.UnboundMethodType
def test_types_UnboundMethodType():
    class A:
        def meth(self):
            pass
    assert isinstance(A.meth, types.UnboundMethodType)
