import codecs
# Test codecs.register_error()

import codecs

def search_function(encoding):
    if encoding == 'test.searchfunction':
        return codecs.lookup('utf-8')
    return None

codecs.register(search_function)

def test(encoding):
    print '%s: ' % encoding,
    try:
        u = unicode('abc\x80', encoding)
    except UnicodeDecodeError:
        print 'UnicodeDecodeError'
    else:
        print repr(u)

test('test.searchfunction')
test('test.searchfunction')
test('test.searchfunction')
test('test.searchfunction')
test('test.searchfunction')
test('test.searchfunction')
test('test.searchfunction')
test('test.searchfunction')
test('test.searchfunction')
test('test.searchfunction')
test('test.searchfunction')
test('test.searchfunction')
test('test.searchfunction')
test('test.searchfunction')
test('test.searchfunction')
test('test.searchfunction')
test('
