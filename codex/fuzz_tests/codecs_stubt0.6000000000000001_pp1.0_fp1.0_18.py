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

# Pick an encoding that doesn't support U+001A
for encoding in ('cp037', 'iso8859_15', 'mac_roman'):
    if encoding in codecs.aliases.aliases:
        encoding = codecs.aliases.aliases[encoding]
        break
else:
    raise ValueError("No encoding found")

# The encoding support U+0000, but not U+001A
encoding_supports_0000 = (encoding in ('cp037', 'mac_roman'))

# Error handling
def check_error_handling(data, errors, expected):
    encoder = codecs.getencoder(encoding)
    decoder = codecs.getdecoder(encoding)

    # Encode
    encoded, consumed = encoder(data, errors)
    if consumed != len(data):
        raise AssertionError("encoder didn't consume all input")
    if encoded != expected:
        raise AssertionError("encoded data does not match expected")
    encoded, consumed = encoder(b'', errors)
    if
