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
    # Check that UnicodeError, UnicodeTranslateError and UnicodeEncodeError
    # are still subclass of ValueError
    if not issubclass(UnicodeError, ValueError):
        print("FAIL: UnicodeError not subclass of ValueError")
    if not issubclass(UnicodeTranslateError, ValueError):
        print("FAIL: UnicodeTranslateError not subclass of ValueError")
    if not issubclass(UnicodeEncodeError, ValueError):
        print("FAIL: UnicodeEncodeError not subclass of ValueError")

    # Check simple error handling in UnicodeEncodeError
    try:
        "\xff".encode("ascii")
    except UnicodeEncodeError as e:
        if str(e) != "'ascii' codec can't encode character '\\xff' in position 0: ordinal not in range(128)":
            print("FAIL: wrong exception string:", str(e))
        if e.encoding != "ascii":
            print("FAIL: wrong exception encoding:", e.encoding)
       
