import codecs
# Test codecs.register_error

def handler(exception):
    return (u'\ufffd', exception.end)

codecs.register_error('test.xmlcharrefreplace', handler)

# Test that the handler is called
s = u'\u1234\u5678'
t = s.encode('ascii', 'test.xmlcharrefreplace')
assert t == u'\ufffd\ufffd'.encode('ascii'), repr(t)

# Test that the handler is called for surrogates
s = u'\ud800\udc00'
t = s.encode('ascii', 'test.xmlcharrefreplace')
assert t == u'\ufffd\ufffd'.encode('ascii'), repr(t)

# Test that the handler is called for surrogates
s = u'\ud800\udc00'
t = s.encode('ascii', 'test.xmlcharrefreplace')
assert t == u'\ufffd\ufffd'.encode('ascii'), repr(t)

# Test that the handler is called
