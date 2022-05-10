import types
# Test types.FunctionType
def test_types_FunctionType():
    def func():
        pass
    assert isinstance(func, types.FunctionType)

# Test types.LambdaType
def test_types_LambdaType():
    func = lambda: None
    assert isinstance(func, types.LambdaType)

# Test types.GeneratorType
def test_types_GeneratorType():
    def gen():
        yield 1
    assert isinstance(gen(), types.GeneratorType)

# Test types.BuiltinFunctionType
def test_types_BuiltinFunctionType():
    assert isinstance(len, types.BuiltinFunctionType)

# Test types.BuiltinMethodType
def test_types_BuiltinMethodType():
    assert isinstance([].append, types.BuiltinMethodType)

# Test types.MethodType
def test_types_MethodType():
    class A(object):
        def meth(self):
            pass
    assert isinstance(A().meth, types.MethodType)

# Test types.UnboundMethodType
def test_types_Un
