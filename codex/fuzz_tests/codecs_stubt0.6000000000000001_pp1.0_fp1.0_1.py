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

def encode_utf8(s):
    return s.encode('utf-8', 'replace')

def encode_utf16(s):
    return s.encode('utf-16', 'replace')

def encode_utf32(s):
    return s.encode('utf-32', 'replace')

def encode_utf8_add_one_codepoint(s):
    return s.encode('utf-8', 'add_one_codepoint')

def encode_utf16_add_one_codepoint(s):
    return s.encode('utf-16', 'add_one_codepoint')

def encode_utf32_add_one_codepoint(s):
    return s.encode('utf-32', 'add_one_codepoint')

def encode_utf8_add_utf16_bytes(s):
    return s.encode('utf-8', 'add_utf16_bytes')

def encode_utf16_add_utf32_bytes(s):
    return s.encode('utf
