import codecs
# Test codecs.register_error()

import codecs
import unittest

class TestRegisterError(unittest.TestCase):

    def test_register_error(self):
        def my_error_handler(exception):
            return (u'', exception.end)

        codecs.register_error('test.myerrorhandler', my_error_handler)
        self.assertEqual(codecs.lookup_error('test.myerrorhandler'),
                         my_error_handler)

    def test_register_error_duplicate(self):
        def my_error_handler(exception):
            return (u'', exception.end)

        codecs.register_error('test.myerrorhandler', my_error_handler)
        self.assertRaises(ValueError, codecs.register_error,
                          'test.myerrorhandler', my_error_handler)

    def test_register_error_bad_name(self):
        def my_error_handler(exception):
            return (u'', exception.end)

        self.assertRaises(TypeError, codecs
