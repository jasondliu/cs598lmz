import codecs

def add_one_codepoint(exc):
    return ("a", exc.start)

def add_utf16_bytes(exc):
    return (b'ab', exc.start)

def add_utf32_bytes(exc):
    return (b'abcd', exc.start)

codecs.register_error("add_one_codepoint", add_one_codepoint)
codecs.register_error("add_utf16_bytes", add_utf16_bytes)
codecs.register_error("add_utf32_bytes", add_utf32_bytes)

class UnicodeDecodeErrorTest(unittest.TestCase):
    def test_decoding_error(self):
        # this is a valid UTF-8 string:
        s = b"abc\xe4\xbd\xa0\xe5\xa5\xbd".decode("utf-8")
        # but if we feed it just a part of it, it'll cause a UnicodeDecodeError:
        self.assertRaises(UnicodeDecodeError, s.encode, "utf-8", "strict", 0, 4)

        # now try the same thing with a custom error handler:
        s = b"abc\xe4\xbd\xa0\xe5\xa5\xbd".decode("utf-8", "add_one_codepoint")
        self.assertEqual(s, "abca")

        # now try the same thing with a custom error handler that returns
        # a tuple with a bytes object:
        s = b"abc\xe4\xbd\xa0\xe5\xa5\xbd".decode("utf-
