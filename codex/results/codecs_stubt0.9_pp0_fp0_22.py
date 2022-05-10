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

def encode(input, errors):
    return ("".join([hex(ord(c)) for c in input]), len(input))

def decode(input, errors):
    output = ""
    for x in input.split():
        output += chr(int(x[2:], 16))
    return (output, len(input))

codecs.register_error("test.decode", decode)
codecs.register_error("test.encode", encode)

for codec in ["utf-8", "utf-16", "utf-32"]:
    # test UnicodeEncodeError
    try:
        codecs.encode("\uffff", codec, "add_one_codepoint")
    except UnicodeEncodeError as exc:
        pass
    else:
        raise RuntimeError("Add 1 codepoint OK for %s" % codec)
    else:
        print(exc)

    # test UnicodeDecodeError
    try:
        codecs.decode(b'\xff\xff', codec, "replace")
    except UnicodeDecodeError as
