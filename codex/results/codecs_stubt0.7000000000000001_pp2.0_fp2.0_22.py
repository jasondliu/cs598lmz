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

def test():
    # Test for bug 434256:  UTF-16 and UTF-32 codecs don't report
    # decoding errors properly.
    for encoding in "utf-16", "utf-16-be", "utf-16-le", "utf-32", "utf-32-be", "utf-32-le":
        try:
            unicode(b'\xff', encoding)
        except UnicodeDecodeError as e:
            print(e)
            print(unicode(b'\xff', encoding, "ignore"))
            print(unicode(b'\xff', encoding, "replace"))
            print(unicode(b'\xff', encoding, "xmlcharrefreplace"))
            print(unicode(b'\xff', encoding, "add_one_codepoint"))
            print(unicode(b'\xff', encoding, "add_utf16_bytes"))
            print(unicode(b'\xff', encoding, "add_utf32_bytes"))

def main():
    test()

if __name__ == "__main__":
    main
