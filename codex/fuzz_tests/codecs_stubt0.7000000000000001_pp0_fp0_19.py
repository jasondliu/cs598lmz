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

    def test_constructor(self):
        err = UnicodeDecodeError("latin1", b"\xff", 1, 2, "ouch")
        self.assertEqual(err.encoding, "latin1")
        self.assertEqual(err.object, b"\xff")
        self.assertEqual(err.start, 1)
        self.assertEqual(err.end, 2)
        self.assertEqual(err.reason, "ouch")

    def test_start_pos(self):
        err = UnicodeDecodeError("latin1", b"\xff", 1, 2, "ouch")
        self.assertEqual(err.start, 1)
        self.assertEqual(err.pos, 1)

    def test_end_pos(self):
        err = UnicodeDecodeError("latin1", b"\xff", 1, 2, "ouch")
        self.assertEqual(err.end, 2)

    def test_attributes(self):
       
