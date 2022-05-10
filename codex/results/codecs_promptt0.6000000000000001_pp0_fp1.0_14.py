import codecs
# Test codecs.register_error('strict', codecs.ignore_errors)
# Test codecs.register_error('ignore', codecs.ignore_errors)
# Test codecs.register_error('replace', codecs.replace_errors)
# Test codecs.register_error('xmlcharrefreplace', codecs.xmlcharrefreplace_errors)
# Test codecs.register_error('backslashreplace', codecs.backslashreplace_errors)
# Test codecs.register_error('namereplace', codecs.namereplace_errors)

class Codec_Tests(unittest.TestCase):

    def test_decode_encode_stateful(self):
        # Issue #1707828: test that encodings that are stateful also
        # work when used with codecs.EncodedFile.
        #
        # This test should be expanded, and the exact meaning of
        # "stateful" should be defined.  For now, we just test a few
        # codecs.
        for encoding in 'utf-16', 'utf-16-be', 'utf-16-le':
            for
