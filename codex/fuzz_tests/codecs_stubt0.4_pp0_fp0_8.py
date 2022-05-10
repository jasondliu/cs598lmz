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

class TestUnicodeDecodeError(unittest.TestCase):
    def test_decode_error(self):
        for encoding in ('utf-8', 'utf-16', 'utf-32'):
            for errors in ('strict', 'replace', 'ignore', 'add_one_codepoint', 'add_utf16_bytes', 'add_utf32_bytes'):
                try:
                    codecs.decode(b'\xff', encoding, errors)
                except UnicodeDecodeError as exc:
                    self.assertEqual(exc.encoding, encoding)
                    self.assertEqual(exc.object, b'\xff')
                    self.assertEqual(exc.start, 0)
                    self.assertEqual(exc.end, 1)
                    self.assertEqual(exc.reason, 'invalid start byte')
                    self.assertEqual(exc.args, (encoding, b'\xff', 0, 1, 'invalid start byte'))
                else:
                    self.fail("UnicodeDecodeError should have been raised")


