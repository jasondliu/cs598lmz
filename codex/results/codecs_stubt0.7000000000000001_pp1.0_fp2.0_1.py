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

data = "a\x80\xe0\x80\x80\xf0\x80\x80\x80"
print(data.encode("ascii"))
print(data.encode("ascii", "ignore"))
print(data.encode("ascii", "replace"))
print(data.encode("ascii", "backslashreplace"))
print(data.encode("ascii", "xmlcharrefreplace"))
print(data.encode("ascii", "add_one_codepoint"))
print(data.encode("ascii", "add_utf16_bytes"))
print(data.encode("ascii", "add_utf32_bytes"))

print(data.encode("utf-8"))
print(data.encode("utf-8", "ignore"))
print(data.encode("utf-8", "replace"))
print(data.encode("utf-8", "backslashreplace"))
print(data.encode("utf-8", "xmlcharrefreplace"))
print(data.en
