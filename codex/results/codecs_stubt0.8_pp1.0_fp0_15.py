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

# With these registered error handlers, all the tests in this file
# should work correctly.

import unittest

class Utf8Test(unittest.TestCase):
    def test_codec(self):
        self.assertEqual(b'\xc3\xa9\n'.decode('utf-8', 'strict'), '\xe9\n')
        self.assertEqual('\xe9\n'.encode('utf-8', 'strict'), b'\xc3\xa9\n')
        self.assertEqual(b'\xc3\xa9 \xc3\xa9 \xc3\xa9 \xc3\xa9'.decode('utf-8', 'strict'),
                         '\xe9 \xe9 \xe9 \xe9')
        self.assertEqual('\xe9 \xe9 \xe9 \xe9'.encode('utf-8', 'strict'),
                         b'\xc3\xa9 \xc3\xa9 \xc3\xa9 \xc3\xa9')

        self.assertEqual
