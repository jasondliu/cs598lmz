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

# unicode_escape and raw_unicode_escape
for encoding in ("unicode_escape", "raw_unicode_escape"):
    for data, expected in [
        (b'\\u1234', '\u1234'),
        (b'\\U00012345', '\U00012345'),
        (b'\\u1234\\u4321', '\u1234\u4321'),
        (b'\\u1234\\U00012345', '\u1234\u12345'),
        (b'\\U00012345\\u1234', '\U00012345\u1234'),
        (b'\\U00012345\\U00012345', '\U00012345\U00012345'),
        (b'\\u1234\\xabcd', '\u1234\xabcd'),
        (b'\\u1234\\n', '\u1234\n'),
        (b'\\u1234\\u', '\u1234\\u'),
        (b'\\u1234\\x', '
