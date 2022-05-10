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

# Test that the codecs.BOM_UTF8 and codecs.BOM_UTF32BE
# constants are valid utf-8/utf-32-be encoded bytes.
for bom in (codecs.BOM_UTF8, codecs.BOM_UTF32BE):
    bom.decode('utf-8')
    bom.decode('utf-32-be')

# Test that decoding the codecs.BOM_UTF32LE constant
# fails with a UnicodeDecodeError.
with raises(UnicodeDecodeError):
    codecs.BOM_UTF32LE.decode('utf-8')

# Test that decoding the codecs.BOM_LE and the
# codecs.BOM_BE constants fails with a UnicodeDecodeError.
for bom in (codecs.BOM_LE, codecs.BOM_BE):
    with raises(UnicodeDecodeError):
        bom.decode('utf-8')

# Test that encoding a Unicode string with the 'utf-8-sig'
# codec results in a BOM (
