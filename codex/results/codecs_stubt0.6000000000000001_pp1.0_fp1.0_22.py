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

def test(encoding, expected):
    print(encoding)
    for decode_f in (lambda s: s.decode(encoding),
                     lambda s: s.decode(encoding, "strict"),
                     lambda s: s.decode(encoding, "ignore"),
                     lambda s: s.decode(encoding, "replace"),
                     lambda s: s.decode(encoding, "add_one_codepoint"),
                     lambda s: s.decode(encoding, "add_utf16_bytes"),
                     lambda s: s.decode(encoding, "add_utf32_bytes")):
        print("\t" + decode_f.__name__)
        try:
            decoded = decode_f(b'\xff')
        except ValueError as e:
            print("\t\tValueError:", e)
        else:
            if decoded != expected:
                print("\t\tError: expected %s, got %s" % (expected, decoded))

test("ascii", "�")

