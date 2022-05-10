import types
# Test types.FunctionType
def f  (): pass
yes = types.FunctionType is callable
test.testO(yes, "test_types -- FunctionType")
# Test types.MethodType
class C (object):
  def f (self): pass
yes = types.MethodType(C.f, None, C) is C().f
test.testO(yes, "test_types -- MethodType")
# Test types.BuiltinFunctionType
yes = types.BuiltinFunctionType is builtin_function_or_method
test.testO(yes, "test_types -- BuiltinFunctionType")
# Test types.BuiltinMethodType
yes = types.BuiltinMethodType is builtin_function_or_method
test.testO(yes, "test_types -- BuiltinMethodType")
# Test types.TypeType
yes = type(int) is types.TypeType
test.testO(yes, "test_types -- TypeType")
# Test types.UnboundMethodType
yes = type(C.f) is types.UnboundMethodType
test.testO(yes, "test_types -- Unbound
