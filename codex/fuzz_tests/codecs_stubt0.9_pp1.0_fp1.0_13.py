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

def try_one(codec, s):
    print("###", codec, ":", s)
    u = s.encode(codec, "strict")
    print("  +strict", u)
    u = s.encode(codec, "add_one_codepoint")
    print("  +add_one_codepoint", u)
    u = s.encode(codec, "replace")
    print("  +replace", u)
    u = s.encode(codec, "add_utf16_bytes")
    print("  +add_utf16_bytes", u)
    u = s.encode(codec, "add_utf32_bytes")
    print("  +add_utf32_bytes", u)
    u = s.encode(codec, "ignore")
    print("  +ignore", u)

# IMO only the first one ('a' can be encoded in latin1) should write
# data to the buffer. The 4 remaining calls should raise
# UnicodeEncodeError.
because_lat
