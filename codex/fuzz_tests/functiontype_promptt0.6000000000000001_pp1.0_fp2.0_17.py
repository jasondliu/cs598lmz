import types
# Test types.FunctionType
def test_function_type():
	def f(): pass
	assert type(f) == types.FunctionType

# Test types.InstanceType
def test_instance_type():
	class A:
		pass
	a = A()
	assert type(a) == A
	assert type(a) != types.InstanceType

# Test types.GeneratorType
def test_generator_type():
	def gen():
		yield 1
	assert type(gen()) == types.GeneratorType

# Test types.LambdaType
def test_lambda_type():
	l = lambda: None
	assert type(l) == types.LambdaType

# Test types.MethodType
def test_method_type():
	class A:
		def meth(self):
			pass
	a = A()
	assert type(a.meth) == types.MethodType

# Test types.ModuleType
def test_module_type():
	import types
	assert type(types) == types.ModuleType

# Test types.UnboundMethod
