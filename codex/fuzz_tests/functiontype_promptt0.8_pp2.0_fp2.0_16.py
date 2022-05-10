import types
# Test types.FunctionType
def test_function_type():
  assert isinstance(lambda x: x, types.FunctionType)

# Test types.LambdaType
def test_lambda_type():
  assert isinstance(lambda x: x, types.LambdaType)


# Test types.BuiltinFunctionType
def test_builtin_function_type():
  assert isinstance(len, types.BuiltinFunctionType)


# Test types.BuiltinMethodType
def test_builtin_method_type():
  assert isinstance(''.split, types.BuiltinMethodType)


# Test types.MethodType
def test_method_type():
  class A(object):
    def f(self):
      pass
  assert isinstance(A().f, types.MethodType)


# Test types.UnboundMethodType
def test_unbound_method_type():
  class A(object):
    def f(self):
      pass
  assert isinstance(A.f, types.UnboundMethodType)


# Test types.MethodDescriptorType
def test_method_descript
