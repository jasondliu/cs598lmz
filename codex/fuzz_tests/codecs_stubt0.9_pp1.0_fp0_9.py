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

class CodecMapTestCase(unittest.TestCase):
    def test_unknown_handler_type(self):
        cmap = codecs.make_identity_dict(range(255))
        with self.assertRaises(ValueError):
            cmap.set_unknown(None)

    def test_unknown_error(self):
        cmap = codecs.make_identity_dict(range(255))
        with self.assertRaises(ValueError) as e:
            cmap.set_unknown("unknown_error")
        self.assertEqual(str(e.exception), "unknown error handler name 'unknown_error'")

    def test_handling(self):
        cmap = codecs.make_identity_dict(range(255))
        cmap.set_unknown("add_one_codepoint")
        n, x = cmap.decode(b'ab', 'strict')
        self.assertEqual(len(n), 1) # 1 surrogate char
        self.assertEqual(x, 1)
        n, x
