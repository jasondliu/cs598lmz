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

# This file doesn't exist.
filename = support.TESTFN + "xxx"

def test_ascii():
    # Big-endian
    f = open(filename, "w")
    f.write("abc\n")
    f.close()

    with open(filename, "rb") as f:
        u = f.read().decode("ascii")
    os.unlink(filename)
    if (u != "abc\n"):
        raise Exception("encoding/decoding of ascii isn't identity")

def test_utf16():
    # Big-endian
    f = open(filename, "wb")
    f.write("\xff\xfe\x61\x00\x62\x00\x63\x00\x0a\x00")
    f.close()

    with open(filename, "rb") as f:
        u = f.read().decode("utf-16")
    os.unlink(filename)
    if (u != "abc\n"):
        print("u =
