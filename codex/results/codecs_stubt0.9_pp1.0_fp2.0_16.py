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

s = u"\ud800"

for codec in [
        "utf-8", "utf-16-be", "utf-16-le", "utf-32-be", "utf-32-le"]:
    res = s.encode(codec, "replace")
    print(res, repr(res))

for codec in [
        "utf-8", "utf-16-be", "utf-16-le", "utf-32-be", "utf-32-le"]:
    res = s.encode(codec, "add_one_codepoint")
    print(res, repr(res))

for codec in [
        "utf-8", "utf-16", "utf-32"]:
    res = s.encode(codec, "add_utf16_bytes")
    print(res, repr(res))

for codec in ["utf-32"]:
    res = s.encode(codec, "add_utf32_bytes")
    print(res, repr(res))
