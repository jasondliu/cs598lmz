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
    import test.support
    verbose = test.support.verbose

    # Test UTF-8
    if verbose:
        print("Testing UTF-8")
    s = "abc\u20ac\u20ac\u20acdef"
    for i in range(len(s)):
        for j in range(i, len(s)):
            if verbose:
                print("Encoding substring", repr(s[i:j]))
            x = s[i:j].encode("utf-8", "strict")
            if verbose:
                print(" to ", repr(x))
            y = x.decode("utf-8", "strict")
            if verbose:
                print(" back to ", repr(y))
            if y != s[i:j]:
                print("Decoding is not idempotent.")
                print("Encoded form:", repr(x))
                print("Decoded form:", repr(y))
                print("Should have been:", repr(s[i
