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

with open(get_data_filename("utf8-4.txt"), "rb") as fp:
    for line in fp:
        try:
            line.decode("utf-8", 'strict')
        except UnicodeDecodeError as exc:
            s = exc.object.decode("utf-8", 'add_one_codepoint')
            s = exc.object.decode("utf-8", 'add_utf16_bytes')
            s = exc.object.decode("utf-8", 'add_utf32_bytes')
            assert exc.object == b"\xB0\x80\x81\x8A"
            assert s == "a�"
            codecs.register_error("add_one_codepoint", add_one_codepoint)
            codecs.register_error("add_utf16_bytes", add_utf16_bytes)
            codecs.register_error("add_utf32_bytes", add_utf32_bytes)
            s = exc.object.decode("utf-8", 'add_one
