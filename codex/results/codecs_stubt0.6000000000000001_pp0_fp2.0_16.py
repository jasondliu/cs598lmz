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

cp932 = codecs.lookup("cp932")
utf_16_le = codecs.lookup("utf_16_le")
utf_32_le = codecs.lookup("utf_32_le")

text = "aあ"

#
# test cp932 incremental encoder
#

# test add_one_codepoint error handler
encoder = cp932.incrementalencoder(errors="add_one_codepoint")
encoded = encoder.encode(text, True)
assert encoded == b"aa\x82\xa0"

# test add_utf16_bytes error handler
encoder = cp932.incrementalencoder(errors="add_utf16_bytes")
encoded = encoder.encode(text, True)
assert encoded == b"aab\x82\xa0"

# test add_utf32_bytes error handler
encoder = cp932.incrementalencoder(errors="add_utf32_bytes")
encoded = encoder.encode(text, True)
assert encoded ==
