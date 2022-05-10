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

class TestBytesErrors(unittest.TestCase):

    def test_add_one_codepoint(self):
        self.assertEqual(b'\xff'.decode('latin-1', 'add_one_codepoint'), 'a')
        self.assertEqual(b'\xff\xff'.decode('utf-16', 'add_one_codepoint'),
                         'a\uffff')
        self.assertEqual(b'\xff\xff\xff\xff'.decode('utf-32', 'add_one_codepoint'),
                         'a\U0000ffff')

    def test_add_utf16_bytes(self):
        # On big-endian machines, the byte from the previous byte is
        # returned. On little-endian machines, the byte from the next byte
        # is returned.
        #
        # No way to know whether an endianness is used, so we simply test
        # that there is something after the invalid byte.
        self.assertEqual(b'\xff'.decode('utf-16',
