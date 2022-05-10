import codecs
# Test codecs.register_error() with a bogus error handler
# Previously caused a segfault

def handler(exc):
    return u"", exc.end

codecs.register_error("bogus", handler)

try:
    u'\U00012345'.encode('ascii', 'bogus')
except UnicodeEncodeError as exc:
    assert exc.object == u'\U00012345'
    assert exc.start == 0
    assert exc.end == 2
    assert exc.reason == 'surrogates not allowed'
    assert exc.encoding == 'ascii'

print('OK')
