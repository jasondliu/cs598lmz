import codecs
# Test codecs.register_error()

def handler(exception):
    print 'handler:', repr(exception)
    return u'', exception.end

codecs.register_error('test', handler)

for encoding in ['ascii', 'latin-1', 'utf-8']:
    print encoding,
    try:
        '\x80'.decode(encoding)
    except UnicodeError, e:
        print e.__class__.__name__, e
    print '%a' % '\x80'.decode(encoding, 'test')

# Test codecs.lookup_error()

def handler(exception):
    print 'handler:', repr(exception)
    return u'', exception.end

codecs.register_error('test', handler)

for encoding in ['ascii', 'latin-1', 'utf-8']:
    print encoding,
    try:
        '\x80'.decode(encoding)
    except UnicodeError, e:
        print e.__class__.__name__, e
   
