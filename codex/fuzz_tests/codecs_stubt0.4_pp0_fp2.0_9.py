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
    # Test all codecs that support the 'replace' error handler
    # and that aren't aliases
    for encoding in sorted(codecs.__dict__):
        if encoding == 'aliases':
            continue
        try:
            encoder = codecs.getencoder(encoding)
        except LookupError:
            continue
        try:
            decoder = codecs.getdecoder(encoding)
        except LookupError:
            continue
        # Test the 'replace' error handler
        for input, expected in [
            ("\xe9", b"?"),
            ("\xe9\xe9", b"???"),
            ("\xe9\xe9\xe9", b"????"),
            ("\xe9\xe9\xe9\xe9", b"?????"),
            ("\xe9\xe9\xe9\xe9\xe9", b"???????"),
            ]:
            encoded, consumed = encoder(input, "replace")
            if consumed != len(input):
                raise TestF
