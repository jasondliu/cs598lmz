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

def check_one_codepoint(exc):
    if not isinstance(exc.object, str):
        raise TypeError("don't know how to handle %r" % exc.object)
    return (exc.object[exc.start:exc.end], exc.end)

def check_utf16_bytes(exc):
    if not isinstance(exc.object, bytes):
        raise TypeError("don't know how to handle %r" % exc.object)
    return (exc.object[exc.start:exc.end], exc.end)

def check_utf32_bytes(exc):
    if not isinstance(exc.object, bytes):
        raise TypeError("don't know how to handle %r" % exc.object)
    return (exc.object[exc.start:exc.end], exc.end)

codecs.register_error("check_one_codepoint", check_one_codepoint)
codecs.register_error("check_utf16_bytes", check_utf16_bytes)
codecs.register_error("check
