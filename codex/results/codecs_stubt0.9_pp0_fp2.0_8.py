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
    def test_basic(self):
        err = UnicodeDecodeError("ascii", b'\xff', 1, 2, "ouch")
        self.assertEqual(err.__str__(), "ouch")
        self.assertEqual(err.encoding, "ascii")
        self.assertEqual(err.object, b'\xff')
        self.assertEqual(err.start, 1)
        self.assertEqual(err.end, 2)
        self.assertEqual(err.reason, "ouch")

        # test constructor with non-ASCII unicode start and end
        err2 = UnicodeDecodeError("ascii", b'\xff', ru("<\u013d>"), ru("<\u0116>"), "ouch")
        self.assertEqual(err2.start, ru("<\u013d>", "ascii"))
        self.assertEqual(err2.end, ru("<\u0116>", "ascii"))

