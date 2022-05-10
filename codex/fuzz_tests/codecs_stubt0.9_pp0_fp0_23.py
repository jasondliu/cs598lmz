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

tests = [
    # add_one_codepoint errors
    ('idna_error0', b'', b'', 'add_one_codepoint'),
    ('idna_error1', b'a', b'a', 'add_one_codepoint'),
    ('idna_error2', b'\xc3\x28', b'a\xc3\x28', 'add_one_codepoint'),
    ('idna_error3', b'\xa0\xa1', b'\xa0a\xa1', 'add_one_codepoint'),
    ('idna_error4', b'\xe2\x28\xa1', b'a\xe2\x28\xa1', 'add_one_codepoint'),
    ('idna_error5', b'\xe2\x82\x28', b'a\xe2\x82\x28', 'add_one_codepoint'),
    ('idna_error6', b'\xf0\x90\x28\xbc', b'a\xf
