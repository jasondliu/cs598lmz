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


class CodecsModuleTest(unittest.TestCase):

    def test_register(self):
        # Issue #11647: registering an error handler function twice should
        # succeed.
        codecs.register_error("test", lambda x: x)
        codecs.register_error("test", lambda x: x)

    def test_lookup_error(self):
        # Issue #11647: registering an error handler by name should succeed.
        codecs.register_error("test", lambda x: x)
        codecs.lookup_error("test")

    def test_encode_decode_error(self):
        for encoding in ("ascii", "utf-8", "utf-16", "utf-32"):
            for exc in (UnicodeEncodeError, UnicodeDecodeError):
                for handler_name in ("strict", "ignore", "replace", "add_one_codepoint", "add_utf16_bytes", "add_utf32_bytes"):
                    e = exc("", "", 0, 0, "")
                    handler = codec
