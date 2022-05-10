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

f = codecs.open("codecs.out", "w", "utf-8", errors="add_one_codepoint")
b = f.buffer
f.write("\\u2603")
b.flush()

f = codecs.open("codecs.out", "w", "utf-16", errors="add_utf16_bytes")
b = f.buffer
f.write("\\u2603")
b.flush()

f = codecs.open("codecs.out", "w", "utf-32", errors="add_utf32_bytes")
b = f.buffer
f.write("\\u2603")
b.flush()

import binascii

with open("codecs.out", "rb") as f:
    print(binascii.hexlify(f.read()))
