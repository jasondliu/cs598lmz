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

print("Add one codepoint when decoding:")
for codec_name in ("utf-8", "utf-16be", "utf-16le", "utf-32be",
                   "utf-32le"):
    print("%12s: %a" % (codec_name,
                       codecs.decode(b"\xff", codec_name, "add_one_codepoint")))

print("Add one codepoint when encoding:")
for codec_name in ("utf-8", "utf-16be", "utf-16le", "utf-32be",
                   "utf-32le"):
    print("%12s: %a" % (codec_name,
                       codecs.encode(b"\xff", codec_name, "add_one_codepoint")))

print("Add two bytes when decoding:")
for codec_name in ("utf-8", "utf-16be", "utf-16le", "utf-32be",
                   "utf-32le"):
    print("%12s: %a" % (cod
