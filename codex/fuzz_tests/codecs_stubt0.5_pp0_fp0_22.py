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

# This is a list of all the codecs that have non-ASCII output.
# We don't test codecs that have ASCII output, because then
# we'd have to worry about whether the output is valid ASCII.

CODECS_UNDER_TEST = [
    ('utf-16', 'utf-16-be', b'\xff\xfe', b'\xfe\xff'),
    ('utf-16', 'utf-16-le', b'\xff\xfe', b'\xfe\xff'),
    ('utf-16-be', 'utf-16', b'\xff\xfe', b'\xfe\xff'),
    ('utf-16-le', 'utf-16', b'\xff\xfe', b'\xfe\xff'),
    ('utf-32', 'utf-32-be', b'\xff\xfe\x00\x00', b'\x00\x00\xfe\xff'),
    ('utf-32', 'utf-32-le', b'\xff\xfe\x00\x00', b
