import codecs
# Test codecs.register_error
class Codec_Test(unittest.TestCase):
    def test_all(self):
        self.assertEqual(codecs.lookup_error('strict'), codecs.strict_errors)
        self.assertEqual(codecs.lookup_error('ignore'), codecs.ignore_errors)
        self.assertEqual(codecs.lookup_error('replace'), codecs.replace_errors)
        self.assertEqual(codecs.lookup_error('xmlcharrefreplace'), codecs.xmlcharrefreplace_errors)
        self.assertEqual(codecs.lookup_error('backslashreplace'), codecs.backslashreplace_errors)
        self.assertEqual(codecs.lookup_error('namereplace'), codecs.namereplace_errors)

        class test_error(UnicodeError):
            pass

        def testhandler(uerr):
            if isinstance(uerr, test_error):
                return (u'', uerr.end)
            else:
                raise TypeError
        codec
