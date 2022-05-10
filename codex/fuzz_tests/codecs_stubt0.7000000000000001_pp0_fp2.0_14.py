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

def convert_to_latin1(exc):
    if not isinstance(exc.object, str) or exc.end - exc.start != 1:
        raise TypeError("don't know how to handle %r" % exc.object)
    return (unichr(exc.object[exc.start]), exc.end)

codecs.register_error("convert_to_latin1", convert_to_latin1)

class Test_UnicodeDecodeError(unittest.TestCase):

    def test_args(self):
        e = UnicodeDecodeError("test", b"\xff", 1, 2, "reason")
        self.assertEqual(e.encoding, "test")
        self.assertEqual(e.object, b"\xff")
        self.assertEqual(e.start, 1)
        self.assertEqual(e.end, 2)
        self.assertEqual(e.reason, "reason")

    def test_str(self):
        e = UnicodeDecodeError("test", b"\xff
