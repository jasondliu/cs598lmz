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

# read all input files and write them back after encoding and decoding
# the input files are supposed to be valid UTF-8 or UTF-16 or UTF-32
# files.

def test_one_file(filename):
    print("testing", filename)
    text = open(filename, "rb").read()
    # print(text)
    for enc in ("utf-8", "utf-16", "utf-16-le", "utf-16-be",
                "utf-32", "utf-32-le", "utf-32-be"):
        try:
            unic = text.decode(enc)
        except UnicodeError:
            # print("UnicodeError converting", filename, "to", enc)
            continue
        new = unic.encode(enc)
        # print(new)
        if text != new:
            print("no roundtrip for", enc)
            print(text)
            print(new)
        for name in ("strict", "ignore", "replace", "add_one_codepoint",
                     "add_utf16_bytes", "
