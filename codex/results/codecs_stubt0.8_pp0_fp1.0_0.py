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

c = codecs.getencoder('utf-16-be')
test_support.run_doctest(c, encoding="utf-16-be")

def test_main():
    with test_support.check_warnings(("", BytesWarning)):
        test_support.run_doctest(c, encoding="utf-16-be")

    test_support.run_doctest(sys.modules[__name__])

if __name__ == "__main__":
    test_main()
