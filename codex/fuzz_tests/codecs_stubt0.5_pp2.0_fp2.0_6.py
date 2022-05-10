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

import sys
if sys.version_info[0] == 2:
    def test_long_string(self):
        # test for issue #1609
        s = '\U0010ffff'
        self.assertEqual(s.encode('utf-8', 'add_one_codepoint'),
                         b'\xf4\x8f\xbf\xbfa')
        self.assertEqual(s.encode('utf-16', 'add_utf16_bytes'),
                         b'\xff\xfeb\x00a\x00b\x00')
        self.assertEqual(s.encode('utf-32', 'add_utf32_bytes'),
                         b'\xff\xfe\x00\x00b\x00\x00\x00cd\x00\x00\x00')
else:
    def test_long_string(self):
        # test for issue #1609
        s = '\U0010ffff'
        self.assertEqual(s.encode('utf-8', 'add_one_cod
