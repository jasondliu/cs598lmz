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

# Test the codecs module

# test the unicode escape codec

# test the raw-unicode-escape codec

# test the unicode-internal codec

# test the latin-1 codec

# test the ascii codec

# test the utf-7 codec

# test the utf-8 codec

# test the utf-16 codec

# test the utf-16-le codec

# test the utf-16-be codec

# test the utf-32 codec

# test the utf-32-le codec

# test the utf-32-be codec

# test the base64_codec

# test the quoted-printable codec

# test the hex codec

# test the uu codec

# test the rot-13 codec

# test the string-escape codec

# test the unicode-escape codec

# test the raw-unicode-escape codec

# test the unicode-internal codec

# test the charmap codec

# test the iso2022_jp codec

# test the
