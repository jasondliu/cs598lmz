import types
# Test types.FunctionType()
Test.assertTrue(types.FunctionType(lambda x: x, globals()) == types.FunctionType)

# Test types.LambdaType()
func = types.FunctionType(lambda x: x, globals())
func = func(lambda x: x)
Test.assertTrue(type(func), types.LambdaType)

# Test types.BuiltinFunctionType()
Test.assertTrue(type(len), types.BuiltinFunctionType)
