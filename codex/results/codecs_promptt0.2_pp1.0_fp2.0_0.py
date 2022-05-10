import codecs
# Test codecs.register_error()

def handler(exception):
    print 'handler:', exception
    return u'\ufffd', exception.end

codecs.register_error('test.lookup', handler)

def test(encoding):
    print encoding
    try:
        u'\udc00'.encode(encoding)
    except UnicodeEncodeError, e:
        print 'UnicodeEncodeError:', e
    print repr(u'\udc00'.encode(encoding, 'test.lookup'))
    print

for encoding in ['ascii', 'latin-1', 'utf-8', 'utf-16']:
    test(encoding)

print 'Done'
