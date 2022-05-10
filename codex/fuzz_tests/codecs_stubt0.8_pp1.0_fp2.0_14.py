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

def check_unicode_encode_error(encoding, errors, expect):
    # Check that UnicodeEncodeError instances return the right
    # attributes.
    uc = 'ab\u1234cd'
    try:
        by = uc.encode(encoding, errors)
    except UnicodeEncodeError as exc:
        if exc.encoding != encoding:
            print("encoding: %s != %s" % (exc.encoding, encoding))
            raise
        if exc.object != uc:
            print("object: %s != %s" % (exc.object, uc))
            raise
        if exc.start != 2:
            print("start: %d != 2" % exc.start)
            raise
        if exc.end != 3:
            print("end: %d != 3" % exc.end)
            raise
        if exc.reason != expect:
            print("reason: %s != %s" % (exc.reason, expect))
            raise
        by = exc.object[exc.start:exc.end]
       
