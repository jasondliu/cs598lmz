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

# UTF-16

with open(TESTFN, "wb") as f:
    f.write(b"\xff\xfe\xab\x00\xcd\x00")

with open(TESTFN, "rb") as f:
    u = f.read().decode("utf-16", "add_one_codepoint")

assert u == "a\uabcd"

# UTF-32

with open(TESTFN, "wb") as f:
    f.write(b"\xff\xfe\x00\x00\xab\x00\x00\x00\xcd\x00\x00\x00")

with open(TESTFN, "rb") as f:
    u = f.read().decode("utf-32", "add_one_codepoint")

assert u == "a\uabcd"

# UTF-16 with surrogate pairs

with open(TESTFN, "wb") as f:
    f.write(b"\xff\xfe\xd8\
