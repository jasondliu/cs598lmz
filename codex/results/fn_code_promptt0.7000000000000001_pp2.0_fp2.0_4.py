fn = lambda: None
# Test fn.__code__ and fn.__globals__
#
class global_ns_Tester(unittest.TestCase):
	@classmethod
	def setUpClass(self):
		# we are using self.assertEqual to compare __code__ and __globals__
		# to allow the above import test to pass, we need to make sure
		# that there are not things in our dictionary that we will not
		# be able to import.
		#
		# we could use a context manager and a try/except, but this
		# is more explicit
		#
		self.old_opt_level = _opt_level
		self.old_assertEqual = _assertEqual

		_assertEqual = self.assertEqual
		_opt_level = 0

	@classmethod
	def tearDownClass(self):
		_opt_level = self.old_opt_level
		_assertEqual = self.old_assertEqual

	def test_global_ns(self):
		self.assertEqual(
