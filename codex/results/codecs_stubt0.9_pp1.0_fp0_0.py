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

for encoding in "utf_8", "utf_16_le", "utf_16_be", "utf_32_le", "utf_32_be":
    print(encoding)
    if encoding.endswith("_le"):
        errors = ['surrogateescape']
        if encoding != "utf_16_le":
            errors.append("add_one_codepoint")
    elif encoding.endswith("_be"):
        errors = ['surrogateescape']
        if encoding != "utf_16_be":
            errors.append("add_one_codepoint")
    elif encoding == "utf_8":
        errors = ['surrogateescape']
        if sys.maxunicode == 0x10ffff:
            errors.append("add_utf32_bytes")
        else:
            errors.append("add_utf16_bytes")
    else:
        # This should never happen
        assert 0, encoding

    for e in errors:
        try:
            exec("r = u'\u61671'.encode('{}
