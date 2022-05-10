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
    # Test for issue #14078
    for encoding in ('utf-16', 'utf-32'):
        for error_handler in ('add_one_codepoint', 'add_utf16_bytes', 'add_utf32_bytes'):
            try:
                codecs.decode('\x00', encoding, error_handler)
            except UnicodeDecodeError as exc:
                print(exc)
                print(exc.start)
                print(exc.end)
                print(exc.object)
                print(exc.reason)
                print(exc.encoding)
                print(exc.args)
                print(exc.__class__)
                print(exc.__class__.__name__)
                print(exc.__class__.__module__)
                print(exc.__class__.__qualname__)
                print(exc.__class__.__bases__)
                print(exc.__class__.__dict__)
                print(exc.__class__.__doc__)
                print(exc.
