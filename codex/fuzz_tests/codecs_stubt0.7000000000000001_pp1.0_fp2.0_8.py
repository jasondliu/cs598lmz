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

# surrogatepass error handler
def add_bogus_utf16_bytes(exc):
    return (b'ab\xff\xfe', exc.start)

if hasattr(codecs, 'register_error'):
    codecs.register_error("add_bogus_utf16_bytes", add_bogus_utf16_bytes)

def add_bogus_utf32_bytes(exc):
    return (b'ab\x00\x00\xff\xfe', exc.start)

if hasattr(codecs, 'register_error'):
    codecs.register_error("add_bogus_utf32_bytes", add_bogus_utf32_bytes)

def add_illegal_utf16_bytes(exc):
    return (b'ab\xff\xfepq', exc.start)

if hasattr(codecs, 'register_error'):
    codecs.register_error("add_illegal_utf16_bytes", add_illegal_utf16_bytes)

def add_illegal_utf
