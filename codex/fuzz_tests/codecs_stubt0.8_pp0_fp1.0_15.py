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

# test_xmlcharrefreplace
with open("utf32.txt", "wb") as f:
    # Replace with a space
    f.write("abc\U00010000def".encode("utf-32-xmlcharrefreplace"))
    # Replace with a surrogate pair
    f.write("abc\U00010000def".encode("utf-16-xmlcharrefreplace"))
    # Replace with a codepoint
    f.write("abc\U00010000def".encode("utf-8-xmlcharrefreplace"))

with open("utf32.txt", "rb") as f:
    r = f.read().decode("utf-32-be")
    assert r == "abc\U00010000defabc\ud800\udc00defabc\U00010000def"

# test_backslashreplace
with open("utf32.txt", "wb") as f:
    f.write("abc\\\U00010000def".encode("utf-8-backslashreplace"))

with open("utf32.txt", "rb") as f:
    r = f
