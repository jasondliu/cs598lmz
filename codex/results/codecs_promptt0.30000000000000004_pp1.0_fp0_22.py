import codecs
# Test codecs.register_error

import codecs

def search_function(encoding):
    if encoding == 'test.searchfunction':
        return codecs.lookup('utf-8')
    return None

codecs.register(search_function)

def test(encoding):
    try:
        print 'Trying', encoding
        u = unicode('abc\xff', encoding)
    except UnicodeDecodeError, e:
        print 'ERROR:', e

test('ascii')
test('test.searchfunction')

# Test codecs.lookup

import codecs

def search_function(encoding):
    if encoding == 'test.searchfunction':
        return codecs.lookup('utf-8')
    return None

codecs.register(search_function)

def test(encoding):
    try:
        print 'Trying', encoding
        u = unicode('abc\xff', encoding)
    except UnicodeDecodeError, e:
        print 'ERROR:', e

test('ascii')
test('test.searchfunction')


