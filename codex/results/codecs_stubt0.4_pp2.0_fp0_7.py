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

# test UTF-8
for enc, dec in [("utf-8", "utf-8"), ("utf-8", "utf-8-sig")]:
    for errors in ["strict", "replace", "ignore", "surrogateescape", "surrogatepass", "add_one_codepoint"]:
        print("encoding", enc, "decoding", dec, "errors", errors)
        for b in [b"abc\x80", b"abc\x80\x80", b"abc\x80\x80\x80", b"abc\x80\x80\x80\x80"]:
            print("  input", b)
            u = b.decode(enc, errors)
            print("  decoded", u)
            b2 = u.encode(dec, errors)
            print("  encoded", b2)
            u2 = b2.decode(dec, errors)
            print("  decoded", u2)
            if u != u2:
                print("  FAILURE")

# test UTF-16

