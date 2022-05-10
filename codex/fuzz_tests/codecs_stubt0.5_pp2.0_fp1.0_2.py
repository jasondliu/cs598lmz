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

def print_as_utf8(s):
    print("UTF-8:", s.encode("utf-8"))

def print_as_utf16(s):
    print("UTF-16:", s.encode("utf-16"))

def print_as_utf32(s):
    print("UTF-32:", s.encode("utf-32"))

def print_as_utf16_be(s):
    print("UTF-16-BE:", s.encode("utf-16-be"))

def print_as_utf32_be(s):
    print("UTF-32-BE:", s.encode("utf-32-be"))

def print_as_utf16_le(s):
    print("UTF-16-LE:", s.encode("utf-16-le"))

def print_as_utf32_le(s):
    print("UTF-32-LE:", s.encode("utf-32-le"))

def print_as_utf16_ex(s):
    print("UTF-16
