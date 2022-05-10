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
    # test unicode input
    for dec in ('utf-8', 'utf-16', 'utf-16-le', 'utf-16-be', 'utf-32', 'utf-32-le', 'utf-32-be'):
        for enc in ('utf-8', 'utf-16', 'utf-16-le', 'utf-16-be', 'utf-32', 'utf-32-le', 'utf-32-be'):
            if dec == 'utf-32-be' and enc != 'utf-32-be':
                continue
            if enc == 'utf-32-be' and dec != 'utf-32-be':
                continue
            # try to build the BOM
            bom = codecs.BOM_UTF8
            if enc in ('utf-16-le', 'utf-32-le'):
                bom = codecs.BOM_UTF16_LE
            elif enc in ('utf-16-be', 'utf-32-be'):
                bom = codecs.BOM_UTF16_BE
            for
