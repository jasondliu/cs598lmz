import codecs
# Test codecs.register_error

import codecs
import unittest

class TestRegisterError(unittest.TestCase):

    def test_register_error(self):
        def handler(exception):
            return (u'', exception.end)
        codecs.register_error('test.myerrorhandler', handler)
        self.assertEqual(codecs.lookup_error('test.myerrorhandler'), handler)
        self.assertRaises(LookupError, codecs.lookup_error, 'test.nosuchhandler')


def test_main():
    test_support.run_unittest(TestRegisterError)

