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

for encoding, errors in [("ascii", "strict"),
                         ("ascii", "add_one_codepoint"),
                         ("utf-8", "strict"),
                         ("utf-8", "add_utf16_bytes"),
                         ("utf-16-le", "strict"),
                         ("utf-16-le", "add_one_codepoint"),
                         ("utf-32-le", "strict"),
                         ("utf-32-le", "add_utf32_bytes")]:
    print("Encoding:", encoding, "Errors:", errors)
    print("First")
    for func in [bytes, bytearray]:
        print("  Decoding", func)
        a = func([ord("a"), ord("\uDC01")])
        # c = codecs.getdecoder(encoding)(a, errors)
        c = codecs.getdecoder(encoding)(a)
        print("  Encoding", func)
        if errors != "strict":
            with self.assertRaises(UnicodeEncodeError)
