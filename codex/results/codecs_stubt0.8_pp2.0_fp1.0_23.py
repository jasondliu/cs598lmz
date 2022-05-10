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
    ('utf-16','1234','1234'),
    ('utf-16','1234\udc00\ud800','1234\udc00\ud800'),
    ('utf-16','\udc00\ud8001234','\ud800\x34\x12'),
    ('utf-16','\udc00\ud800', None),
    ('utf-16','1234\udc00', None),
    ('utf-16','1234\ud800', None),
    ('utf-16','\ud8001234', None),
    ('utf-32','1234','1234'),
    ('utf-32','1234\udc00\ud800','1234\udc00\ud800'),
    ('utf-32','\udc00\ud8001234','\ud800\x34\x12'),
    ('utf-32','\udc00\ud800', None),
    ('utf-32','1234\udc00', None),
    ('utf-32','1234\ud800', None),
    ('utf-
