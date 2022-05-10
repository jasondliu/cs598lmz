import types
# Test types.FunctionType, types.GeneratorType, types.BuiltinFunctionType, and type

# Tests for __instancecheck__:

def test():
	assert isinstance(lambda x: 1, types.FunctionType)
	assert issubclass(types.FunctionType, object)
	assert not isinstance(42, types.FunctionType)

	def function():
		pass

	assert isinstance(function, types.FunctionType)
	assert not issubclass(types.FunctionType, types.FunctionType)


	def generator():
		yield 42

	gen = generator()
	assert isinstance(gen, types.GeneratorType)
	assert isinstance(gen, types.GeneratorType)
	assert isinstance(gen, types.GeneratorType)
	assert not isinstance(function, types.GeneratorType)
	assert isinstance(print, types.BuiltinFunctionType)
	assert not isinstance(function, types.BuiltinFunctionType)
	assert isinstance(print, type(print))


# test Python code
print("Test code")
print(isinstance(lambda:print,
