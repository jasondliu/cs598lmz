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

def check(exc, codec, function,
          start, end, reason, input, name=None):
    print("exception:", exc)
    print("reason:", reason)
    print("input", input)
    print("start:", start, "end:", end)
    print("function:", function)
    if name is not None:
        print("encoding:", name)

# codec = codecs.lookup("ascii")
# codec.error = check

for name in ("ascii", "utf-8"):
    codec = codecs.lookup(name)
    codec.error = check
    codec.encode("abc\x80def", "replace")
    codec.encode("abc\x80def", "ignore")
    codec.encode("abc\x80def", "xmlcharrefreplace")
    codec.encode("abc\x80def", "backslashreplace")
    codec.encode("abc\x80def", "add_one_codepoint")
    if name == "ascii":
       
