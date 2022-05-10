import codecs
# Test codecs.register_error()

import codecs

def handler(exception):
    print 'handler:', exception
    return u'', exception.end

codecs.register_error('test.lookup', handler)

def test(encoding):
    print encoding, ':',
    try:
        u'\udc00'.encode(encoding, 'test.lookup')
    except UnicodeEncodeError, e:
        print 'UnicodeEncodeError:', e
    except UnicodeTranslateError, e:
        print 'UnicodeTranslateError:', e

for encoding in ['ascii', 'latin-1', 'utf-8', 'utf-16']:
    test(encoding)

# Test codecs.register_error() with a function

import codecs

def handler(exception):
    print 'handler:', exception
    return u'', exception.end

def test(encoding):
    print encoding, ':',
    try:
        u'\udc00'.encode(encoding, handler)
    except UnicodeEn
