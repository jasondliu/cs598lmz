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

# test the error handlers
for enc in ["utf-8", "utf-16", "utf-32"]:
    print(enc)
    for handler in ["strict", "ignore", "replace", "add_one_codepoint", "add_utf16_bytes", "add_utf32_bytes"]:
        print(handler)
        print(codecs.decode(b'\xff', enc, errors=handler))
        print(codecs.decode(b'\xff\xff', enc, errors=handler))
        print(codecs.decode(b'\xff\xff\xff', enc, errors=handler))
        print(codecs.decode(b'\xff\xff\xff\xff', enc, errors=handler))

# test the error handlers
for enc in ["utf-8", "utf-16", "utf-32"]:
    print(enc)
    for handler in ["strict", "ignore", "replace", "add_one_codepoint", "add_utf16_bytes", "add_utf32_bytes"]:

