import codecs
# Test codecs.register_error()

import codecs

def handler(exception):
    print 'Error handler called with %s' % exception

codecs.register_error('test.lookup', handler)

def test(name):
    print 'Testing %s:' % name
    try:
        codecs.lookup(name)
    except LookupError, e:
        print '  LookupError: %s' % e

test('test.lookup')
test('test.lookup_error')
test('test.lookup_function')
test('test.lookup_function_error')
test('test.lookup_exception')
test('test.lookup_exception_error')
test('test.lookup_object')
test('test.lookup_object_error')
test('test.lookup_object_not_found')
test('test.lookup_object_not_found_error')
test('test.lookup_object_bad_getitem')
test('test.lookup_object_bad_getitem_error')
test('test.lookup_
