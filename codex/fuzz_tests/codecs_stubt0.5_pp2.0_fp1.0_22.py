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
    def test_utf8_errors(self):
        self.assertEqual(b'\xe4\xb8\xad\xea\xb3\xa0\xe5\xad\x97',
                         b'\xe4\xb8\xad\xff\xb3\xa0\xe5\xad\x97'.decode('utf-8', 'replace'))
        self.assertEqual(b'\xe4\xb8\xad\xea\xb3\xa0\xe5\xad\x97',
                         b'\xe4\xb8\xad\xff\xb3\xa0\xe5\xad\x97'.decode('utf-8', 'ignore'))
        self.assertEqual(b'\xe4\xb8\xad\xea\xb3\xa0\xe5\xad\x97',
                         b'\xe4\xb8\xad\xff\xb3\xa0\xe5\xad\x97
