import codecs
# Test codecs.register_error
def codec_error_encode_callback(exc):
    if isinstance(exc, UnicodeEncodeError):
        target_charset = exc.encoding
        text = exc.object
        start = exc.start
        end = exc.end
        return u"", start+1

class TestUnicode(unittest.TestCase):

    def testCodecsModule(self):
        self.assertTrue(codecs.BOM_UTF8=='\xef\xbb\xbf')
        self.assertTrue(codecs.BOM_UTF16_LE=='\xff\xfe')
        self.assertTrue(codecs.BOM_UTF16_BE=='\xfe\xff')
        self.assertTrue(codecs.BOM_UTF32_LE=='\xff\xfe\x00\x00')
        self.assertTrue(codecs.BOM_UTF32_BE=='\x00\x00\xfe\xff')
        self.assertTrue(codecs.BOM == codecs.
