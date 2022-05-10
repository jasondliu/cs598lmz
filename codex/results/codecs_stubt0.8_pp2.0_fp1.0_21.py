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

class CodecsModuleTest(unittest.TestCase):

    def test_register_error(self):
        s = 'pi\u00f1ata'
        for encoding in 'utf-8', 'utf-16', 'utf-32':
            self.assertRaises(UnicodeDecodeError, s.encode, encoding, 'surrogateescape')
            try:
                s.encode(encoding, 'add_one_codepoint')
            except UnicodeDecodeError:
                self.fail('UnicodeDecodeError should not be raised')
            try:
                s.encode(encoding, 'add_utf16_bytes')
            except UnicodeDecodeError:
                self.fail('UnicodeDecodeError should not be raised')
            if encoding == 'utf-16':
                self.assertRaises(UnicodeDecodeError, s.encode, encoding, 'add_utf32_bytes')
            else:
                try:
                    s.encode(encoding, 'add_utf32_bytes')
                except UnicodeDecodeError
