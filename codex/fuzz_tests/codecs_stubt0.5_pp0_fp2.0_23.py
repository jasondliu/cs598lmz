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

    def test_doc_example(self):
        # Test the example from the docstring
        s = b'pi: \u03c0'
        try:
            s.decode('ascii')
        except UnicodeDecodeError as e:
            self.assertEqual(e.object, s)
            self.assertEqual(e.start, 4)
            self.assertEqual(e.end, 6)
            self.assertEqual(e.reason, 'disallowed character')
            self.assertEqual(e.encoding, 'ascii')
            self.assertEqual(e.args, (s, 4, 6, 'disallowed character', 'ascii'))
            self.assertEqual(e.__str__(),
                             "'ascii' codec can't decode byte 0xcf in position 4: disallowed character")
            # XXX: should this be documented?
            self.assertEqual(e.__unicode__(),
                             "'ascii
