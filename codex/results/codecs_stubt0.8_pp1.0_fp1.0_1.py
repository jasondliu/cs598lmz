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
    tests = [('utf-8', '\xf5[\xf5\xc3\xb5]), (b'\xf5[\xf5\x45\xf5\x45', '\xf5[\xf5\xc3\xb5\xc3\x95\xc3\x95', 'add_one_codepoint'), ('utf-16', b'\xff\xfe\x00\xd8\x00\xdc[\x00\xd8\x00\xdc\x01\xda', '\U0001d11e[\U0001d11e\U0001d11e\U0001d128', 'add_utf16_bytes'), ('utf-32', b'\xff\xfe\x00\x00\x00\xd8\x00\x00\x00\xdc[\x00\x00\x00\xd8\x00\x00\x00\xdc\x01\x00\x00\x00', '\U0001d11e[\U0001d11e\
