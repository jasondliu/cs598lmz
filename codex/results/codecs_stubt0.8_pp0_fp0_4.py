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

N_CHARACTERS = 1024

def string_to_unicode(text, encoding, errors="strict"):
    u"""Converts `text` in the given `encoding` to a Unicode string.
    """
    assert isinstance(text, str)
    if encoding == "utf-8":
        # Because of bugs in Python's UTF-8 and BOM handling, we manually
        # convert UTF-8 here.
        assert isinstance(text, str)
        if text.startswith(u'\ufeff'):
            # Python uses the BOM as the encoding if it is present, so we need
            # to strip it before converting.
            text = text[1:]

        # When running tests with the Python executable, we want to ensure that
        # UTF-8-encoded bytes are decoded into Unicode characters. Python's
        # character encoding system doesn't behave this way, so we need to
        # manually decode the bytes by hand.
        output = io.BytesIO(text.encode('utf-8'))
        stdin = io.TextIOWrapper
