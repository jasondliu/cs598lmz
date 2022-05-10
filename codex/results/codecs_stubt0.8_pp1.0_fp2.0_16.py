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

def test_main():
    import sys

    if sys.platform == "win32":
        err = 'strict'
    else:
        err = 'surrogateescape'

    def test(name, enc, bytes, error, unicode):
        print("%20s"%name, end='')
        sys.stdout.flush()
        try:
            if bytes is None:
                bytes = unicode.encode(enc, error)
            text = bytes.decode(enc, error)
            assert text == unicode
        except Exception as e:
            print("\nEncoding: %s\nError handler: %s\nInput: %r\nException: %r\n"%(enc, error, unicode, e))
        else:
            print(" OK")

    all_errors = ("strict", "ignore", "replace", "xmlcharrefreplace",
                  "backslashreplace", "namereplace", "surrogateescape")

    for error in all_errors:
        # standard encoding
        test("ascii, %s"
