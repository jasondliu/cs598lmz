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

# test encoding
s = '\ud800\udc00'
for errors in ["strict", "add_one_codepoint", "add_utf16_bytes", "add_utf32_bytes"]:
    res = s.encode("utf-16-le", errors)
    for i in range(0, len(res)-1, 2):
        assert res[i] == b"\x00" and res[i+1] == b"\x00"

for errors in ["strict", "add_one_codepoint", "add_utf16_bytes", "add_utf32_bytes"]:
    res = s.encode("utf-16-be", errors)
    for i in range(0, len(res)-1, 2):
        assert res[i] == b"\x00" and res[i+1] == b"\x00"

for errors in ["strict", "add_one_codepoint", "add_utf16_bytes", "add_utf32_bytes"]:
    res = s.encode("utf
