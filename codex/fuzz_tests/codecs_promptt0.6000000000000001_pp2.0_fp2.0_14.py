import codecs
# Test codecs.register_error

# This test checks whether the 'register_error' function of the
# 'codecs' module is working as expected.

class Codec_Test(unittest.TestCase):
    def test_register_error(self):
        import codecs
        self.assertEqual(codecs.register_error('test.xmlcharrefreplace',
                                               codecs.xmlcharrefreplace_errors),
                         codecs.xmlcharrefreplace_errors)

        self.assertEqual(codecs.register_error('test.backslashreplace',
                                               codecs.backslashreplace_errors),
                         codecs.backslashreplace_errors)

        self.assertEqual(codecs.register_error('test.namereplace',
                                               codecs.namereplace_errors),
                         codecs.namereplace_errors)

        self.assertRaises(LookupError,
                          codecs.register_error, 'test.unknown',
                          codecs.xmlcharrefreplace_errors)

        self.assertRaises(TypeError,
                          codec
