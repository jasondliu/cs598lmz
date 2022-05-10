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

# This tests the following:
#     - unicode-internal codec support
#     - decoding of invalid bytes
#     - decoding of invalid UCS-2 bytes
#     - decoding of invalid UTF-32 bytes
#     - decoding of invalid UCS-2 surrogate pairs
#     - decoding of invalid UTF-32 surrogate pairs
#     - decoding of truncated UTF-8 bytes
#     - decoding of truncated UTF-16 bytes
#     - decoding of truncated UTF-32 bytes
#     - decoding of truncated UTF-8 surrogate pairs
#     - decoding of truncated UTF-16 surrogate pairs
#     - decoding of truncated UTF-32 surrogate pairs
#     - decoding of truncated UCS-2 surrogate pairs
#     - decoding of truncated UTF-32 surrogate pairs
#     - decoding of UTF-8 and UTF-16 BOMs
#     - decoding of UTF-32 BOMs and their endianness
#     - decoding of UTF-16 BOMs and their endianness
#     - decoding of UTF-8 surrogates
#     - decoding of UTF-16 surrogates
#     - decoding of UTF-32 surrog
