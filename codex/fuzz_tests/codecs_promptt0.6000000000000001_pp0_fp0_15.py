import codecs
# Test codecs.register_error

def handler(exception):
    print(exception)
    return (u"\ufffd", exception.end)

codecs.register_error("test.ignore", handler)
codecs.register_error("test.replace", handler)
codecs.register_error("test.xmlcharrefreplace", handler)
codecs.register_error("test.backslashreplace", handler)

# unicode-escape and raw-unicode-escape are tested in test_unicode.py

def test(encoding):
    print(encoding)

    # Encode
    s = "abc\u1234def"
    try:
        x = s.encode(encoding, "strict")
    except UnicodeError:
        print("can't encode")
    else:
        print(x)
        print(x.decode(encoding))

    for error in "ignore", "replace", "xmlcharrefreplace", "backslashreplace":
        print(error)
        x = s.encode(encoding, error)
        print(x
