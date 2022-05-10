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

def errmsg_basic(e, name):
    """Return the error message that should be shown after *e*."""
    msg = "can't decode bytes in position %d-%d: %s\n" \
          % (e.start, e.end, e.reason)
    if e.start == e.end == 0 and e.reason == 'bad continuation byte':
        msg += ": invalid start byte"
    return msg

def errmsg_translate(e, name):
    msg = "can't translate bytes in position %d-%d: %s\n" \
          % (e.start, e.end, e.reason)
    return msg

def errmsg_to_surrogate(e, name):
    msg = "can't encode bytes in position %d-%d: %s" \
          % (e.start, e.end, e.reason)
    return msg

def errmsg_from_surrogate(e, name):
    msg = "can't decode bytes in position %d-%d: %s" \

