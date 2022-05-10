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


def fix_utf16(exc):
    return ("\u1234", exc.start)

def fix_utf32(exc):
    return ("\U00012345", exc.start)

codecs.register_error("fix_utf16", fix_utf16)
codecs.register_error("fix_utf32", fix_utf32)


def check_encode(input, errors, expected):
    got = input.encode("utf-8", errors=errors)
    if got != expected:
        print("encode failed for", errors, repr(input))
        print("encoded as", repr(got))
        print("expected", repr(expected))
        return False
    return True

def check_decode(input, errors, expected):
    got = input.decode("utf-8", errors=errors)
    if got != expected:
        print("decode failed for", errors, repr(input))
        print("decoded as", repr(got))
        print("expected", repr(expected))
        return False
    return True

def
