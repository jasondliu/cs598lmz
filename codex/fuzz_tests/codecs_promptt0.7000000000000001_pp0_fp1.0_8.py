import codecs
# Test codecs.register_error
# Error handling with unknown codec name
import codecs

def codec_error_handler(exception):
    return ("", exception.end)

codecs.register_error("test.error", codec_error_handler)

class Test_Codecs(unittest.TestCase):
    def test_decode_errors(self):
        # Test the various decode error handling methods
        errors = [
            "strict",
            "ignore",
            "replace",
            "xmlcharrefreplace",
            "backslashreplace",
            "namereplace",
            "test.error"
        ]
        x = "abc\u0141\u0142\u0143def"
        for enc in ("ascii", "latin-1"):
            for err in errors:
                try:
                    codecs.decode(x, enc, err)
                except (UnicodeError, LookupError):
                    pass
                else:
                    self.fail("%s/%s did not raise exception" % (enc, err))

    def test_encode
