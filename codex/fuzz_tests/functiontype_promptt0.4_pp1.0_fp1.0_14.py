import types
# Test types.FunctionType
def test_function_type():
    assert isinstance(test_function_type, types.FunctionType)
# Test types.LambdaType
test_lambda_type = lambda: None
assert isinstance(test_lambda_type, types.LambdaType)
# Test types.BuiltinFunctionType
assert isinstance(len, types.BuiltinFunctionType)
# Test types.BuiltinMethodType
assert isinstance(len, types.BuiltinMethodType)
# Test types.MethodType
class A(object):
    def __init__(self):
        self.b = 1
    def test(self):
        pass
a = A()
assert isinstance(a.test, types.MethodType)
# Test types.UnboundMethodType
assert isinstance(A.test, types.UnboundMethodType)
# Test types.ModuleType
assert isinstance(types, types.ModuleType)
# Test types.TracebackType
def test_traceback_type():
    try:
        1/0
    except Exception as e:
        assert isinstance(e.__traceback
