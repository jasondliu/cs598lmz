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

# test bad input: invalid character
for encoding in ["utf-8", "utf-16", "utf-16-be", "utf-16-le",
                 "utf-32", "utf-32-be", "utf-32-le"]:
    try:
        codecs.charmap_encode(u'\uFFFE', "strict", encoding)
    except UnicodeEncodeError as err:
        print(encoding, err)

# test bad input: truncated character
for encoding in ["utf-8", "utf-16", "utf-16-be", "utf-16-le",
                 "utf-32", "utf-32-be", "utf-32-le"]:
    try:
        codecs.charmap_encode(u'\U0010FFFF', "strict", encoding)
    except UnicodeEncodeError as err:
        print(encoding, err)

# test bad input: character out of range
for encoding in ["latin-1", "iso8859-1", "iso8859-15", "ascii",
