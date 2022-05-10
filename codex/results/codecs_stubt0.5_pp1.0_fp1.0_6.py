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

# The following tests are copied from test_codecs.py
# with the addition of a replacement function
# that adds a codepoint.

import codecs, sys

def test_surrogates():
    # Error handling for surrogates
    for enc in ('utf-16', 'utf-16-le', 'utf-16-be'):
        for t in (0xD800, 0xDFFF):
            for c in (0xDC00, 0xD800, 0xDFFF, 0xDBFF):
                for f in (int, lambda x: x.decode(enc)):
                    raises(UnicodeDecodeError, f, b'\x00' + chr(t) + chr(c))

def test_errors():
    # Test encoding/decoding with various error handlers
    for encoding in ('utf-16', 'utf-16-be', 'utf-16-le'):
        for errors in ('strict', 'ignore', 'replace',
                       'xmlcharrefreplace', 'backslashreplace',
                       'add_
