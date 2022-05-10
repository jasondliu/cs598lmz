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

import sys, encodings
encodings._cache["add_one_codepoint"] = "utf_8"
encodings._cache["add_utf16_bytes"] = "utf_16_le"
encodings._cache["add_utf32_bytes"] = "utf_32_le"

codecs.register_error("test.test_codecs.test_surrogates", add_one_codepoint)
encodings._cache["test.test_codecs.test_surrogates"] = "utf_8"

class Test_UTF8(unittest.TestCase):
    def test_utf8_decode(self):
        self.assertEqual(
            "\xe4\xf6\xfc".encode("utf-8").decode("utf-8"),
            "\xe4\xf6\xfc"
        )
        self.assertRaises(UnicodeDecodeError,
                          "\xe4\xf6\xfc\xfc".encode("utf-8").decode, "utf-8")
