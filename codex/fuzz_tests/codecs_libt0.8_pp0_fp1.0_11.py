import codecs
codecs.register(lambda name: name == 'cp65001' and codecs.lookup('utf-8') or None) # for stdout and stderr

class Test(unittest.TestCase):
	def test_no_exceptions(self):
		def foo(f):
			return f()

		def bar():
			raise Exception()

		self.assertRaises(Exception, foo, bar)

if __name__ == '__main__':
	unittest.main()
