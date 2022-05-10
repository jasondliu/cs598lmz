import types
# Test types.FunctionType
class functiontype_test:
	def f(self, x):
		return x
	def test_function(self):
		assert type(self.f) == types.FunctionType
		assert type(self.f).__name__ == 'function'
		assert type(self.f).__module__ == 'types'
		assert type(self.f).__bases__ == (object,)
	def test_function_with_defaults(self):
		def f(self, x=1):
			return x
		assert type(f) == types.FunctionType
		assert type(f).__name__ == 'function'
		assert type(f).__module__ == 'types'
		assert type(f).__bases__ == (object,)
	def test_function_with_keywords(self):
		def f(self, x=1):
			return x
		assert type(f) == types.FunctionType
		assert type(f).__name__ == 'function'
		assert type(f
