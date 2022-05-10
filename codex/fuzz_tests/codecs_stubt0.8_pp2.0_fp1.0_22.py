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

some_strs = [
    chr(0xFFFF),
    chr(0xFFFF) + chr(0xFFFF),
    chr(0xFFFF) + chr(0xFFFF) + chr(0xFFFF),
    chr(0xFFFF) + chr(0xFFFF) + chr(0xFFFF) + chr(0xFFFF),
    # Surrogate code points:
    chr(0xD800),
    chr(0xD7FF),
    chr(0xDBFF),
    chr(0xDC00),
    chr(0xDFFF),
    chr(0xD800) + chr(0xD7FF),
    chr(0xDBFF) + chr(0xDC00),
    chr(0xDFFF) + chr(0xDFFF),
    chr(0xD800) + chr(0xD7FF) + chr(0xD800),
    chr(0xD7FF) + ch
