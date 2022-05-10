import codecs
# Test codecs.register_error
# This test is copied from test_codecs.py, because it was failing
# when run under regrtest.py.

class CodecTest(unittest.TestCase):

    def test_register_error(self):
        # 'strict' error handler
        self.assertRaises(UnicodeError, unicode, 'Andr\202 x', 'ascii')
        # register a replacement handler
        codecs.register_error('test.replace', codecs.replace_errors)
        try:
            # now encoding works
            u = unicode('Andr\202 x', 'ascii', 'test.replace')
            self.assertEqual(u, u'Andr\uFFFD x')
        finally:
            # cleanup
            del codecs.lookup_error['test.replace']
        # 'strict' error handler is back again
        self.assertRaises(UnicodeError, unicode, 'Andr\202 x', 'ascii')


def test_main():
    test_support.run_unittest(Codec
