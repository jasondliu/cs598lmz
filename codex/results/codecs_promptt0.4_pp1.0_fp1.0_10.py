import codecs
# Test codecs.register_error()

import codecs

def handler(exception):
    print 'handler:', exception
    return u'', exception.end

codecs.register_error('test', handler)

def test(encoding):
    print encoding, ':',
    try:
        u'\udc80'.encode(encoding)
    except UnicodeEncodeError, e:
        print 'UnicodeEncodeError:', e
    else:
        print 'no error'

test('ascii')
test('latin-1')
test('utf-8')
test('test')

# Test codecs.lookup()

import codecs

def test(encoding):
    try:
        codecs.lookup(encoding)
    except LookupError, e:
        print 'LookupError:', e
    else:
        print encoding, 'found'

test('ascii')
test('latin-1')
test('utf-8')
test('test')

# Test codecs.getencoder()

import codecs
