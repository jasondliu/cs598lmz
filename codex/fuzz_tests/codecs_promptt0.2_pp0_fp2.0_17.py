import codecs
# Test codecs.register_error

import codecs
import unittest

class TestRegisterError(unittest.TestCase):
    def test_register_error(self):
        def my_error_handler(exception):
            return (u'', exception.end)
        codecs.register_error('test.myerrorhandler', my_error_handler)
        self.assertEqual(codecs.lookup_error('test.myerrorhandler'),
                         my_error_handler)
        self.assertRaises(LookupError, codecs.lookup_error, 'test.xxx')
        codecs.register_error('test.myerrorhandler', None)
        self.assertRaises(LookupError, codecs.lookup_error, 'test.myerrorhandler')

def test_main():
    test_support.run_unittest(TestRegisterError)

if __name__ == "__main__":
    test_main()
