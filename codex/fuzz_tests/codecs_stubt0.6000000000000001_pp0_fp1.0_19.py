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

class UnicodeInternalTest(unittest.TestCase):
    def test_decoding_UTF16_BE(self):
        # Issue #7402: UTF16-BE decoding failed with UnicodeDecodeError
        # if the last character was invalid.
        self.assertEqual('\ufffd', '\x00\x80'.decode('UTF-16BE', 'replace'))
        self.assertEqual('\ufffd', '\x00\x80'.decode('UTF-16', 'replace'))
        self.assertEqual('\ufffd', '\x00\x80'.decode('UTF-16-BE', 'replace'))
        self.assertEqual('\ufffd', '\x00\x80'.decode('UTF-16LE', 'replace'))
        self.assertEqual('\ufffd', '\x00\x80'.decode('UTF-16-LE', 'replace'))

    def test_decoding_UTF16_LE(self):
        # Issue #7402: UTF16-LE decoding failed with UnicodeDecodeError
       
