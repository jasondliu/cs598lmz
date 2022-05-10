import types
# Test types.FunctionType
test_function = types.FunctionType(compile('a + b', '<string>', 'eval'),
                                   globals(), 'test_function')
test_function(1, 2)

# Test types.ClassType
test_class = types.ClassType('TestClass', (), {})
test_class()

# Test types.UnboundMethodType
class TestUnboundMethod:
    def test_unbound_method(self):
        pass
test_unbound_method = types.UnboundMethodType(TestUnboundMethod.test_unbound_method,
                                              None, TestUnboundMethod)
test_unbound_method()

# Test types.MethodType
test_method = types.MethodType(TestUnboundMethod.test_unbound_method,
                               TestUnboundMethod())
test_method()

# Test types.BuiltinFunctionType
test_builtin_function = types.BuiltinFunctionType(int)
test_builtin_function('42')

# Test types.BuiltinMethodType
class TestBuiltinMethod:
    def __int__
