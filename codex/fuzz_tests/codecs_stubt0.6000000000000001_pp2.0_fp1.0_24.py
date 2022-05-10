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

# Test decoding with add_one_codepoint
try:
    '\udc00'.encode('utf-8', 'add_one_codepoint')
except UnicodeEncodeError as exc:
    assert exc.object == '\udc00'
    assert exc.start == 0
    assert exc.end == 1
    assert exc.reason == 'incomplete surrogate'
    assert str(exc) == 'incomplete surrogate at end of string'

try:
    '\ud800\udc00'.encode('utf-8', 'add_one_codepoint')
except UnicodeEncodeError as exc:
    assert exc.object == '\ud800\udc00'
    assert exc.start == 0
    assert exc.end == 2
    assert exc.reason == 'incomplete surrogate'
    assert str(exc) == 'incomplete surrogate at end of string'

try:
    '\ud800\udc00'.encode('utf-16', 'add_one_codepoint')
except UnicodeEncodeError as exc:
    assert exc.object ==
