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

def test(codec, data, add_bytes=False):
    print("\nCodec:", codec)
    print("data:", data.encode("unicode_escape"))
    print("encoded:", codec.encode(data, "surrogateescape")[0])
    print("decoded:", codec.decode(codec.encode(data, "surrogateescape")[0],
                                   "surrogateescape"))
    if add_bytes:
        print("encoded (add_utf16_bytes):",
              codec.encode(data, "add_utf16_bytes")[0])
        print("decoded (add_utf16_bytes):",
              codec.decode(codec.encode(data, "add_utf16_bytes")[0],
                           "add_utf16_bytes"))
    print("encoded (add_one_codepoint):",
          codec.encode(data, "add_one_codepoint")[0])
    print("decoded (add_one_codepoint):",
