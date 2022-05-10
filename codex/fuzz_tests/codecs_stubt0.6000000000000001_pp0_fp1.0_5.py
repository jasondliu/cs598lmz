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

def test(name, enc):
    print("=== {} ===".format(name))
    print(enc.getregentry())
    print()
    print("'\u1234'", enc.encode('\u1234'))
    print(repr(enc.encode('\u1234', 'strict')))
    print(repr(enc.encode('\u1234', 'add_one_codepoint')))
    print(repr(enc.encode('\u1234', 'add_utf16_bytes')))
    print(repr(enc.encode('\u1234', 'add_utf32_bytes')))
    print()
    print("'\u1234'", enc.decode('\u1234'))
    print(repr(enc.decode(b'\xff', 'strict')))
    print(repr(enc.decode(b'\xff', 'add_one_codepoint')))
    print(repr(enc.decode(b'\xff', 'add_utf16
