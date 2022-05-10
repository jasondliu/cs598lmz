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

# utf-8 decoder

try:
    '\udc80'.encode('utf-8', 'add_one_codepoint')
except UnicodeEncodeError as exc:
    print(exc)
try:
    b'\xed\xb2\x80'.decode('utf-8', 'add_one_codepoint')
except UnicodeDecodeError as exc:
    print(exc)

# utf-16-be decoder

try:
    '\udc80'.encode('utf-16-be', 'add_utf16_bytes')
except UnicodeEncodeError as exc:
    print(exc)
try:
    b'\xdc\x80'.decode('utf-16-be', 'add_utf16_bytes')
except UnicodeDecodeError as exc:
    print(exc)

# utf-16-le decoder

try:
    '\udc80'.encode('utf-16-le', 'add_utf16_bytes')
except UnicodeEncodeError as exc:
    print(exc
