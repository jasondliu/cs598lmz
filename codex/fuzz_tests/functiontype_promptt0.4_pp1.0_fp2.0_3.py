import types
# Test types.FunctionType
def test_FunctionType():
    def f():
        pass
    assert type(f) is types.FunctionType
    assert type(f) is types.BuiltinFunctionType

# Test types.BuiltinFunctionType
def test_BuiltinFunctionType():
    assert type(len) is types.BuiltinFunctionType

# Test types.MethodType
def test_MethodType():
    class Foo:
        def f(self):
            pass
    assert type(Foo().f) is types.MethodType

# Test types.UnboundMethodType
def test_UnboundMethodType():
    class Foo:
        def f(self):
            pass
    assert type(Foo.f) is types.UnboundMethodType

# Test types.LambdaType
def test_LambdaType():
    assert type(lambda x: x) is types.LambdaType

# Test types.GeneratorType
def test_GeneratorType():
    def f():
        yield 1
    assert type(f()) is types.GeneratorType

# Test types.CodeType
def
