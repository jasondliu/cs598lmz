import codecs
# Test codecs.register_error
# This covers part of the tests in test_codecs.py

class Test_register_error(unittest.TestCase):
    def test_register_errors(self):
        self.assertRaises(TypeError, codecs.register_error, None)
        self.assertRaises(LookupError, codecs.register_error, "spam")
        codecs.register_error("test", lambda: 42)
        self.assertEqual(codecs.lookup_error("test"), 42)
        codecs.register_error("test", lambda: 24)
        self.assertEqual(codecs.lookup_error("test"), 24)

def test_main():
    test_support.run_unittest(Test_register_error)

if __name__ == "__main__":
    test_main()
