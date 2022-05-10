import types
# Test types.FunctionType
def test_function_type():
    def f(x):
        return x*2

    assert type(f) == types.FunctionType
test_function_type()
# Test types.LambdaType
def test_lambda_type():
    f = lambda x: x*2

    assert type(f) == types.LambdaType
test_lambda_type()
# Test types.CodeType
def test_code_type():
    def f(x):
        return x*2

    assert type(f.__code__) == types.CodeType
test_code_type()
# Test types.MethodType
def test_method_type():
    class A:
        def f(self, x):
            return x*2

    a = A()
    assert type(a.f) == types.MethodType
test_method_type()
# Test types.BuiltinFunctionType
# This is the type for built-in functions like "len"
def test_builtin_function_type():
    assert type(len) == types.BuiltinFunctionType
test_builtin
