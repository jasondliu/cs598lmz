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

# Test for the UTF-8 codec

# Test for the UTF-16 codec

# Test for the UTF-32 codec

# Test for the UTF-16-LE codec

# Test for the UTF-16-BE codec

# Test for the UTF-32-LE codec

# Test for the UTF-32-BE codec

# Test for the UTF-16-ex codec

# Test for the UTF-32-ex codec

# Test for the UTF-7 codec

# Test for the UTF-8-SIG codec

# Test for the UTF-16-LE-SIG codec

# Test for the UTF-16-BE-SIG codec

# Test for the UTF-32-LE-SIG codec

# Test for the UTF-32-BE-SIG codec

# Test for the UTF-8-variants codec

# Test for the UTF-16-variants codec

# Test for the UTF-32-variants codec

# Test for the UTF-7-variants codec

# Test for the UTF-8-variants-with-BOM codec
