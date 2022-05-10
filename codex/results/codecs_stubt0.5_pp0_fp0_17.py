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

class TestCodecs(unittest.TestCase):

    def test_utf_16_le_decode(self):
        self.assertEqual('abc', 'abc'.encode('utf-16-le').decode('utf-16-le'))
        self.assertEqual('abc', 'abc'.encode('utf-16-le').decode('utf-16-le', errors='ignore'))
        self.assertEqual('ab\ufffd', 'abc'.encode('utf-16-le').decode('utf-16-le', errors='replace'))
        self.assertEqual('ab\ufffdc', 'abc'.encode('utf-16-le').decode('utf-16-le', errors='replace',
                                                                      replace='\ufffd'))
        self.assertEqual('ab\ufffd', 'abc'.encode('utf-16-le').decode('utf-16-le', errors='replace',
                                                                      replace='\ufffd\ufffd'))
        self.assertEqual('ab\ufffd',
