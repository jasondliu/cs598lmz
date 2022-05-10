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

# test the add_one_codepoint error handler
try:
    u'\u20ac'.encode('ascii')
except UnicodeEncodeError as exc:
    print(repr(exc.object))
    print(exc.reason)
    print(exc.start)
    print(exc.end)
    print(exc.encoding)
    print(exc.object[exc.start:exc.end])
    print('-')
    print(repr(exc.object.encode('ascii', 'add_one_codepoint')))
    print()

# test the add_utf16_bytes error handler
try:
    u'a\U0010ffff'.encode('utf-16')
except UnicodeEncodeError as exc:
    print(repr(exc.object))
    print(exc.reason)
    print(exc.start)
    print(exc.end)
    print(exc.encoding)
    print(exc.object[exc.start:exc.end])
    print('-')
    print(repr(
