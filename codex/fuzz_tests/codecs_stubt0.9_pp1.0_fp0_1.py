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

try:
    unicode.encode(b"abcd", "utf-8")
except UnicodeEncodeError as exc:
    import ipdb; ipdb.set_trace()


def my_replace(exc):
    if isinstance(exc, UnicodeEncodeError):
        if len(exc.object[exc.start:exc.end]) == 1:
            return (b'ab', exc.start)
    return (exc, exc.start)


codecs.register_error("replace_bytes", my_replace)
