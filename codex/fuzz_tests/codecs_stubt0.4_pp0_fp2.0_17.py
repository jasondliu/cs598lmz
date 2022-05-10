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
    # test that utf-8-sig skips the BOM
    for bom in (b'\xef\xbb\xbf', b'\xfe\xff', b'\xff\xfe'):
        for encoding in ('utf-8-sig', 'utf-16', 'utf-16-le', 'utf-16-be',
                         'utf-32', 'utf-32-le', 'utf-32-be'):
            for errors in ('strict', 'ignore', 'replace', 'add_one_codepoint',
                           'add_utf16_bytes', 'add_utf32_bytes'):
                s = bom + codecs.BOM_UTF8 + codecs.BOM_UTF16_LE + codecs.BOM_UTF16_BE + codecs.BOM_UTF32_LE + codecs.BOM_UTF32_BE
                if errors == 'strict':
                    assertRaises(UnicodeError, s.decode, encoding)
                else:
                    s.decode(encoding
