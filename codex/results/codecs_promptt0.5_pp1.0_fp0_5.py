import codecs
# Test codecs.register_error
# See SF bug #1533245

import codecs

def handler(exception):
    return (u'\ufffd', exception.end)

codecs.register_error('test.xmlcharrefreplace', handler)

s = u'\u1234'

def test(encoding):
    print encoding
    print codecs.encode(s, encoding, 'test.xmlcharrefreplace')

test('ascii')
test('utf-8')
test('latin-1')
