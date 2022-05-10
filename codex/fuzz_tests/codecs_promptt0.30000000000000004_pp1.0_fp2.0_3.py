import codecs
# Test codecs.register_error

def handler(exception):
    return (u'', exception.end)

codecs.register_error('test.xmlcharrefreplace', handler)

s = u'\u1234\u5678'

for encoding in ['ascii', 'utf-8', 'utf-16']:
    encoded = s.encode(encoding, 'test.xmlcharrefreplace')
    decoded = encoded.decode(encoding)
    print repr(encoded), repr(decoded)
    assert decoded == u'', "decoded should be empty"
