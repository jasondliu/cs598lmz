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

# utf-16-be

try:
    u'\udc00'.encode('utf-16-be')
except UnicodeEncodeError as exc:
    print_exc(exc)
    print(exc.object.encode('utf-16-be', 'add_one_codepoint'))
    print(exc.object.encode('utf-16-be', 'add_utf16_bytes'))

try:
    u'\ud800\udc00'.encode('utf-16-be')
except UnicodeEncodeError as exc:
    print_exc(exc)
    print(exc.object.encode('utf-16-be', 'add_one_codepoint'))
    print(exc.object.encode('utf-16-be', 'add_utf16_bytes'))

# utf-16-le

try:
    u'\udc00'.encode('utf-16-le')
except UnicodeEncodeError as exc:
    print_exc(exc)
    print(exc.object.encode('
