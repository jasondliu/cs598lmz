import codecs
# Test codecs.register_error
try:
    codecs.register_error
except AttributeError:
    print('SKIP')
    raise SystemExit

# Test the backslashreplace error handler
def test_backslashreplace_handler(encoding, msg):
    try:
        codecs.encode(msg, encoding)
    except UnicodeEncodeError as e:
        print(repr(e.object))
        print(e.start, e.end)
        print(repr(e.reason))
        print(repr(e.encoding))
        print(repr(e.object[e.start:e.end]))
        print(repr(e.object[e.start:e.end].encode(e.encoding, 'backslashreplace')))

test_backslashreplace_handler('ascii', 'abc\u1234def')
test_backslashreplace_handler('ascii', 'abc\ud800def')
test_backslashreplace_handler('ascii', 'abc\udc00def')
test_backslashreplace
