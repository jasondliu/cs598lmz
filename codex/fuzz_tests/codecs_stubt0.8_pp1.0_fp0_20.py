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

def test():
    for encoding in ('utf-8', 'utf-16', 'utf-32'):
        add_one_codepoint_text = codecs.encode("\u1002", encoding, 'add_one_codepoint')
        add_one_codepoint_result = codecs.decode(add_one_codepoint_text.decode(encoding), encoding)
        if add_one_codepoint_result != "\u1002a":
            print("add_one_codepoint failed for encoding " + encoding)
        add_utf16_bytes_text = codecs.encode("\u1002", encoding, 'add_utf16_bytes')
        add_utf16_bytes_result = codecs.decode(add_utf16_bytes_text.decode(encoding), encoding)
        if add_utf16_bytes_result != "\u1002ab":
            print("add_utf16_bytes failed for encoding " + encoding)
        add_utf32_bytes_text = codecs.encode("\u1002
