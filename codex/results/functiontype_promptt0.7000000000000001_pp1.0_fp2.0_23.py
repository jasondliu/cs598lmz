import types
# Test types.FunctionType
def test_types_functionType():
   def f(x):
      return x
   def g(x):
      return x
   assert isinstance(f, types.FunctionType)
   assert isinstance(g, types.FunctionType)
   assert isinstance(test_types_functionType, types.FunctionType)
   assert isinstance(test_types_functionType.__code__, types.CodeType)
   assert isinstance(test_types_functionType.__globals__, dict)
   assert isinstance(test_types_functionType.__closure__, tuple)

# Test types.LambdaType
def test_types_lambdaType():
   f = lambda x: x
   assert isinstance(f, types.LambdaType)
   assert isinstance(f.__code__, types.CodeType)
   assert isinstance(f.__globals__, dict)
   assert isinstance(f.__closure__, tuple)

def test_types_methodType():
   class A(object):
      def f(self, x):
         return
