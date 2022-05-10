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

class CodecTestBase(unittest.TestCase):

    test_cases = ()

    def test_decode(self):
        for name, enc, utf8 in self.test_cases:
            for errors in "strict", "ignore", "replace", "add":
                b = utf8
                n = len(b)
                if errors == "add":
                    if enc.startswith("utf-16-"):
                        b = b"\xff\xfe" + b
                    elif enc.startswith("utf-32-"):
                        b = b"\xff\xfe\x00\x00" + b
                    b += b"\xff"
                    n += 3
                s = utf8.decode(enc)
                self.assertEqual(s.encode(enc, errors), b)
                b += b"\xff\xff"
                n += 2
                s = b.decode(enc, errors)
                self.assertEqual(s.encode(enc), utf8)
                self.assertEqual(len
