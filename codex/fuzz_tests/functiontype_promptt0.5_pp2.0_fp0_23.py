import types
# Test types.FunctionType

def test_func_type():
    def foo():
        pass
    assert type(foo) == types.FunctionType

# Test types.BuiltinFunctionType

def test_builtin_func_type():
    assert type(abs) == types.BuiltinFunctionType

# Test types.MethodType

def test_method_type():
    class Foo:
        def foo(self):
            pass
    assert type(Foo().foo) == types.MethodType

# Test types.UnboundMethodType

def test_unbound_method_type():
    class Foo:
        def foo(self):
            pass
    assert type(Foo.foo) == types.UnboundMethodType

# Test types.LambdaType

def test_lambda_type():
    assert type(lambda: None) == types.LambdaType

# Test types.GeneratorType

def test_generator_type():
    def foo():
        yield
    assert type(foo()) == types.GeneratorType

# Test types.CodeType

def test_code
