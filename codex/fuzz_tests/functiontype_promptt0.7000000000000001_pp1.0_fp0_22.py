import types
# Test types.FunctionType
class TestTypes(unittest.TestCase):
	def test_function_type(self):
		def f():
			pass
		self.assertTrue(type(f) == types.FunctionType)
		# Test __builtins__
		self.assertTrue(hasattr(__builtins__, '__import__'))
		# In python2, the following is not true
		#self.assertTrue(type(__builtins__) == types.ModuleType)

if __name__ == '__main__':
	unittest.main()
