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

# bug 429: custom replace errors cause
#   UnicodeDecodeError: 'utf8' codec can't decode bytes in position 0-1: unexpected code byte
# if the Unicode string returned by the callback contains an illegal
# sequence.

for enc in "utf-8", "utf-16-le", "utf-32-le":
    for err in "add_one_codepoint", "add_utf16_bytes", "add_utf32_bytes":
        print("decoding", repr("x\xFF"), "with", enc, "and", err)
        print("utf-8:", repr(b'x\xFF'.decode(enc, err)))
