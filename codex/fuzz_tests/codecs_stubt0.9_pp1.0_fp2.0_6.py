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
    u'a\uDC00'.encode('utf-8', 'add_one_codepoint')
except UnicodeEncodeError as exc:
    print(exc.object)
    print(exc.start)
    print(exc.end)
    print(exc.reason)
    print(exc.encoding)

print()
try:
    bytes('a\uDC00', 'utf-16', 'strict').decode('utf-8', 'add_utf16_bytes')
except UnicodeDecodeError as exc:
    print(exc.object)
    print(exc.start)
    print(exc.end)
    print(exc.reason)
    print(exc.encoding)

print()
try:
    bytes('a\uDC00', 'utf-32', 'strict').decode('utf-8', 'add_utf32_bytes')
except UnicodeDecodeError as exc:
    print(exc.object)
    print(exc.start)
    print(exc.end)
    print(exc.reason)
   
