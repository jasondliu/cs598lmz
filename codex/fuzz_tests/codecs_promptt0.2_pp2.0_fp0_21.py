import codecs
# Test codecs.register_error

import codecs
import unittest

class TestRegisterError(unittest.TestCase):
    def test_register_error(self):
        def handler(exception):
            return (u'', exception.end)
        codecs.register_error('test.strict', handler)
        self.assertEqual(codecs.lookup_error('test.strict'), handler)
        codecs.register_error('test.strict', None)
        self.assertEqual(codecs.lookup_error('test.strict'), None)

def test_main():
    test_support.run_unittest(TestRegisterError)

if __name__ == "__main__":
    test_main()
