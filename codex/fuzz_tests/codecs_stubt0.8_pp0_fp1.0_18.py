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

tests = (
        (b'\x00', 'utf-16-le', "utf-16-le"),
        ('\u1234', 'utf-16', "utf-16-be"),
        ('\u1234', 'utf-16-be', "utf-16-be"),
        ('\u1234', 'utf-16-le', "utf-16-le"),
        ('\u1234', 'utf-32', "utf-32-be"),
        ('\u1234', 'utf-32-be', "utf-32-be"),
        ('\u1234', 'utf-32-le', "utf-32-le"),
        ('\u1234', 'utf-16-ex', "utf-16-ex"),
        ('\u1234', 'utf-16-le-ex', "utf-16-le-ex"),
        ('\u1234', 'utf-16-be-ex', "utf-16-be-ex"),
        ('\u1234', 'utf-32-ex', "utf-32-ex"),
        ('
