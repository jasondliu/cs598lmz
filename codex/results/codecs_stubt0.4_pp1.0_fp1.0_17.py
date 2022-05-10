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

    def test_encode_decode_error_handling(self):
        self.assertEqual(
            "abc",
            "ab".decode("ascii", "add_one_codepoint")
        )
        self.assertEqual(
            "abc",
            "ab".decode("utf-16", "add_utf16_bytes")
        )
        self.assertEqual(
            "abc",
            "ab".decode("utf-32", "add_utf32_bytes")
        )
        self.assertEqual(
            "abc",
            "ab".decode("ascii", "add_one_codepoint")
        )
        self.assertEqual(
            "abc",
            "ab".decode("utf-16", "add_utf16_bytes")
        )
        self.assertEqual(
            "abc",
            "ab".decode("utf-32", "add_utf32_bytes")
        )

    def test
