import codecs
# Test codecs.register_error()

def handler(exception):
    print 'got', exception
    return u'', exception.end

codecs.register_error('test.lookup', handler)

# Encoding
print codecs.encode('abc\u20ac', 'ascii', 'test.lookup')
print codecs.encode('abc\u20ac', 'ascii', 'test.lookup')
print codecs.encode('abc\u20ac', 'ascii', 'test.lookup')

# Decoding
print codecs.decode('abc\x80', 'ascii', 'test.lookup')
print codecs.decode('abc\x80', 'ascii', 'test.lookup')
print codecs.decode('abc\x80', 'ascii', 'test.lookup')

# Test codecs.lookup_error()

def handler(exception):
    print 'got', exception
    return u'', exception.end

codecs.lookup_error('test.lookup')

# Enc
