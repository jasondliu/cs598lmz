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

if __name__ == "__main__":
    def test_one_codepoint(encoding):
        print("testing", encoding)
        u = chr(0xFFFF)
        s = u.encode(encoding)
        print("input:", s)
        print("output:", s.decode(encoding, "add_one_codepoint"))
        print()

    def test_two_bytes(encoding):
        print("testing", encoding)
        u = b'\xFF\xFF'
        s = u.decode(encoding)
        print("input:", s)
        print("output:", s.encode(encoding, "add_utf16_bytes"))
        print()

    def test_four_bytes(encoding):
        print("testing", encoding)
        u = b'\xFF\xFF\xFF\xFF'
        s = u.decode(encoding)
        print("input:", s)
        print("output:", s.encode(encoding, "add_utf32
