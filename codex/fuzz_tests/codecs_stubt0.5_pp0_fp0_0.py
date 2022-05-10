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

def test(encoding, test_string, errors):
    try:
        encoded_string = test_string.encode(encoding, errors)
    except UnicodeEncodeError as e:
        print(e)
    else:
        print(encoded_string)
        print(encoded_string.decode(encoding, errors))

test("ascii", "abc\uFFFD\uFFFD", "ignore")
test("ascii", "abc\uFFFD\uFFFD", "replace")
test("ascii", "abc\uFFFD\uFFFD", "xmlcharrefreplace")
test("ascii", "abc\uFFFD\uFFFD", "backslashreplace")
test("ascii", "abc\uFFFD\uFFFD", "namereplace")
test("ascii", "abc\uFFFD\uFFFD", "add_one_codepoint")

test("utf-16", "abc\uFFFD\uFFFD", "ignore")
test("utf-16", "abc\u
