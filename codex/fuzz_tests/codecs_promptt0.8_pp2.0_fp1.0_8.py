import codecs
# Test codecs.register_error agains some codecs which support error handlers
# As of Unicode 3.2, some codecs don't yet work with the new error handling.
# See SF bug #947043.
import string

class CodecTest(unittest.TestCase):
    def test_encode(self):
        for name in "utf_7 utf_8 utf_16 utf_16_be utf_16_le".split():
            codecs.lookup(name).encode("abc", "xmlcharrefreplace")
            codecs.lookup(name).encode("abc", "xmldefault")
            codecs.lookup(name).encode("abc", "xmlcharrefreplace")
            codecs.lookup(name).encode("abc", "strict")
            codecs.lookup(name).encode("abc", "replace")
            codecs.lookup(name).encode("abc", "ignore")
            codecs.lookup(name).encode("abc", "backslashreplace")
            # Unsupported:
            #codecs.lookup(
