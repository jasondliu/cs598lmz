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

def test_main():
    from test import test_support
    import sys
    import os
    import encodings
    from encodings import utf_8, utf_16, utf_16_be, utf_16_le, utf_32, utf_32_be, utf_32_le
    from encodings import utf_16_ex, utf_32_ex
    from encodings import unicode_internal
    from encodings import base64_codec
    from encodings import hex_codec
    from encodings import quopri_codec
    from encodings import uu_codec
    from encodings import rot_13

    # test the utf-8 codec
    utf8 = utf_8.getregentry()
    s = u'\u20ac\u2026\u2039'
    assert utf8.encode(s) == '\xe2\x82\xac\xe2\x80\xa6\xe2\x80\xb9'
   
