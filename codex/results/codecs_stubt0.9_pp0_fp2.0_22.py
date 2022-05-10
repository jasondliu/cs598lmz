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
    '\ud8ff'.encode('utf-32le', 'add_one_codepoint')
except UnicodeEncodeError as e:
    print(e)

try:
    '\ud8ff'.encode('UTF-16', 'add_utf16_bytes')
except UnicodeEncodeError as e:
    print(e)

try:
    '\ud8ff'.encode('UTF-32', 'add_utf32_bytes')
except UnicodeEncodeError as e:
    print(e)
