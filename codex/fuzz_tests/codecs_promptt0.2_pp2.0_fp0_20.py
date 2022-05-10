import codecs
# Test codecs.register_error()

def handler(exception):
    print 'handler:', exception
    return u'\ufffd', exception.end

codecs.register_error('test.lookup', handler)

def test(encoding):
    print encoding, ':',
    try:
        u'\u1111'.encode(encoding, 'test.lookup')
    except UnicodeEncodeError, exception:
        print 'UnicodeEncodeError:', exception
    else:
        print 'no exception'

for encoding in ['ascii', 'latin-1', 'utf-8', 'utf-16']:
    test(encoding)

# Test codecs.lookup_error()

def test(encoding):
    print encoding, ':',
    try:
        u'\u1111'.encode(encoding, 'test.lookup')
    except UnicodeEncodeError, exception:
        print 'UnicodeEncodeError:', exception
    else:
        print 'no exception'

for encoding in ['ascii', 'latin-1
