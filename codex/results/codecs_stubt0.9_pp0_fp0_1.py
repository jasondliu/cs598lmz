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

print(b"123 \xe4\xb8\xad\xe6\x96\x87".decode(
    "utf-8", errors="add_one_codepoint"))
print(b"123 \xd8\x90\xe5\x8d\x88".decode(
    "utf-16-le", errors="add_utf16_bytes"))
print(
    b"\x00\x00\x03\xe8\x00\x00\x18\xd8\x00\x00\x02\xdf".decode(
        "utf-32-le", errors="add_utf32_bytes"))
