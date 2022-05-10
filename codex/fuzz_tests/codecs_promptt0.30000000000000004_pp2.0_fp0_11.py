import codecs
# Test codecs.register_error()

import codecs

def handler(exception):
    return (u'', exception.end)

codecs.register_error('test.ignore', handler)

# test with unicode
assert codecs.decode('abc\x80', 'ascii', 'test.ignore') == u'abc'
assert codecs.decode('abc\x80', 'ascii', 'test.ignore') == u'abc'

# test with bytes
assert codecs.decode(b'abc\x80', 'ascii', 'test.ignore') == u'abc'
assert codecs.decode(b'abc\x80', 'ascii', 'test.ignore') == u'abc'

# test with bytearray
assert codecs.decode(bytearray(b'abc\x80'), 'ascii', 'test.ignore') == u'abc'
assert codecs.decode(bytearray(b'abc\x80'), 'ascii', 'test.ignore') == u'abc'

# test with memory
