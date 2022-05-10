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

GOOD_UTF8 = b'\xed\xa0\x80\xed\xb0\x80'
GOOD_UTF32BE = b'\x00\x00\xed\xa0\x00\x00\xed\xb0'
GOOD_UTF16BE = b'\xed\xa0\x00\xed\xb0\x00'
GOOD_UTF32LE = b'\xa0\x00\x00\xed\x00\x00\x00\xed'
GOOD_UTF16LE = b'\x00\xa0\x00\xed\x00\xb0\x00\xed'

BAD_UTF32BE = b'\x00\x00\xed\xa0\x00\x00\xed'
BAD_UTF16BE = b'\xed\xa0\x00\xed\xb0'

class TestUTF8CharmapState(unittest.TestCase):
    encoding = 'utf-8'
    utf16_
