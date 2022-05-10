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

def test_utf16_surrogates():
    # This can be "a\udc00" in UTF-32.
    for name in ["utf-16-be", "utf-16-le"]:
        e = codecs.getencoder(name)
        d = codecs.getdecoder(name)
        s = "ab\uD83D\uDE02"
        for errors in [None, "strict", "ignore", "replace", "add_one_codepoint",
                       "add_utf32_bytes"]:
            with self.subTest(name=name, errors=errors):
                # Encode.
                r = e(s, errors=errors)
                if errors == "strict":
                    self.assertRaises(UnicodeEncodeError, e, s)
                elif errors == "replace":
                    self.assertEqual(len(r[0]), 6)
                    self.assertEqual(r[0], b"\xff\xfea\xff\xff\xfe")
                    self.assertEqual(r[
