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

# Test that the codecs module can be imported and that it has
# the expected attributes

import codecs

assert hasattr(codecs, 'BOM_UTF8')
assert hasattr(codecs, 'BOM_UTF16')
assert hasattr(codecs, 'BOM_UTF16_BE')
assert hasattr(codecs, 'BOM_UTF16_LE')
assert hasattr(codecs, 'BOM_UTF32')
assert hasattr(codecs, 'BOM_UTF32_BE')
assert hasattr(codecs, 'BOM_UTF32_LE')

assert hasattr(codecs, 'BOM')
assert hasattr(codecs, 'BOM_BE')
assert hasattr(codecs, 'BOM_LE')

assert hasattr(codecs, 'BOM_UTF8')
assert hasattr(codecs, 'BOM_UTF16')
assert hasattr(codecs, 'BOM_UTF16_BE')
assert hasattr(codecs, 'BOM_
