import codecs
# Test codecs.register_error()

import codecs

def search_function(encoding):
    if encoding == 'test.searchfunction':
        return codecs.lookup('utf-8')
    return None

codecs.register(search_function)

def test(encoding):
    try:
        print 'Trying', encoding
        u = unicode('abc', encoding)
    except LookupError, err:
        print 'ERROR:', err

test('test.searchfunction')
test('test.searchfunction2')

# Test codecs.lookup()

import codecs

def test(encoding):
    try:
        print 'Trying', encoding
        u = unicode('abc', encoding)
    except LookupError, err:
        print 'ERROR:', err

test('utf-8')
test('utf-16')
test('utf-16-be')
test('utf-16-le')
test('utf-32')
test('utf-32-be')
test('utf-32-le')
test('utf-7')
test('utf-
