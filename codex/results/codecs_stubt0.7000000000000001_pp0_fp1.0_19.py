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
    failures = []
    for encoding in ('utf-8', 'utf-8-sig', 'utf-7', 'utf-32-be', 'utf-32-le', 'utf-32', 'utf-16-be', 'utf-16-le', 'utf-16'):
        try:
            u = '\u20ac\ufffe'.decode(encoding)
            try:
                u.encode(encoding)
            except UnicodeEncodeError:
                pass
            else:
                failures.append(encoding)
        except ValueError:
            pass
    assert not failures, "encode() succeeded for %s after decode() failed" % (failures,)

    for encoding in ('ascii', 'utf-8', 'utf-8-sig', 'utf-7', 'utf-32-be', 'utf-32-le', 'utf-32', 'utf-16-be', 'utf-16-le', 'utf-16'):
        try:
            u = '\u20ac\ufffe'.decode(
