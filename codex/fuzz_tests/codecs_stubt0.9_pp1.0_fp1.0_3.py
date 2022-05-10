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

unistr = chr(0x1234) + chr(0xABCD)

# unicode -> utf-32 roundtrip
for errors in "strict", "replace", "ignore", "add_one_codepoint":
    assert unistr.encode("utf-32", errors) == unistr.encode("utf-32"), errors

# unicode -> utf-16 roundtrip
for errors in "strict", "replace", "ignore", "add_utf16_bytes":
    assert unistr.encode("utf-16", errors) == unistr.encode("utf-16"), errors

# unicode -> utf-32 -> utf-16 roundtrip
for errors in "strict", "replace", "ignore", "add_utf16_bytes":
    assert unistr.encode("utf-32", errors).decode("utf-16") == unistr, errors

# unicode -> utf-32 -> utf-8 roundtrip
for errors in "strict", "replace", "ignore", "add_utf32_
