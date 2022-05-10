import codecs
# Test codecs.register_error()

import codecs

def handler(exception):
    print 'handler:', exception
    return u'\ufffd', exception.end

codecs.register_error('test.myerror', handler)

def test(encoding):
    print encoding, ':',
    try:
        u'\u1111'.encode(encoding)
    except UnicodeEncodeError, e:
        print 'UnicodeEncodeError:', e
    try:
        '\xff'.decode(encoding)
    except UnicodeDecodeError, e:
        print 'UnicodeDecodeError:', e

for encoding in ['ascii', 'latin-1', 'test.myerror']:
    test(encoding)

# Test codecs.lookup()

import codecs

def test(encoding):
    print encoding, ':',
    try:
        codecs.lookup(encoding)
    except LookupError, e:
        print 'LookupError:', e

for encoding in ['ascii', 'latin
