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

data = 'a\xe9'

print("original:", repr(data))
utf8_encoded = str.encode("utf-8", errors="replace", data=data)
print("utf-8 replace: ", repr(utf8_encoded))
utf8_encoded = str.encode("utf-8", errors="add_one_codepoint", data=data)
print("utf-8 add_one_codepoint:", repr(utf8_encoded))

utf16_encoded = str.encode("utf-16", errors="replace", data=data)
print("utf-16 replace:", repr(utf16_encoded))
utf16_encoded = str.encode("utf-16", errors="add_utf16_bytes", data=data)
print("utf-16 add_utf16_bytes:", repr(utf16_encoded))

utf32_encoded = str.encode("utf-32", errors="replace", data=data)
print("utf-32 replace:", repr(utf32_encoded))
utf32_enc
