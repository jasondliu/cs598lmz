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

def check(encoding, input, exc_type, errorhandler, expected_result):
    codecs.register_error("strict", exc_type)
    codecs.register_error("ignore", lambda exc: ("", exc.start))
    codecs.register_error("replace", lambda exc: ("?", exc.start))
    for errors in ("strict", "ignore", "replace", errorhandler):
        got = input.encode(encoding, errors)
        if got != expected_result:
            print("%s.encode(%r, errors=%r) returned %r; "
                  "expected %r" % (repr(input), encoding, errors,
                                   got, expected_result))
        got = expected_result.decode(encoding, errors)
        if got != input:
            print("%r.decode(%r, errors=%r) returned %r; "
                  "expected %r" % (expected_result, encoding, errors,
                                   got, input))

for encoding in ("utf-8", "utf-16", "utf
