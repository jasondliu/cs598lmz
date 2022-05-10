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

with open("utf16_codepoint.txt", "wb") as f:
    f.write(codecs.encode(unicode_data, "utf-16", "add_utf16_bytes"))

with open("utf32_codepoint.txt", "wb") as f:
    f.write(codecs.encode(unicode_data, "utf-32", "add_utf32_bytes"))

unicode_data = unicode_data.replace(u'\uffff', u'\u0fff')
with open("utf32_0x0fff.txt", "wb") as f:
    f.write(codecs.encode(unicode_data, "utf-32", "add_one_codepoint"))

# This is the worst case for the UTF-16 decoder.
unicode_data = unicode_data.replace(u'\u0fff', u'\u0D7FF')
with open("utf16_0xd7ff.txt", "wb") as f:
    f.write(codecs
