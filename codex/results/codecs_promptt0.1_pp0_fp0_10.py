import codecs
# Test codecs.register_error

import codecs

def handler(exception):
    print 'handler called'
    return (u'', exception.end)

codecs.register_error('test.lookup', handler)

# Test the basic functionality
print 'Test 1'
print codecs.lookup_error('test.lookup')

# Test that the handler is called
print 'Test 2'
codecs.lookup_error('test.lookup')('abc', 0, 1, 'test')

# Test that the handler is called
print 'Test 3'
codecs.lookup_error('test.lookup')('abc', 0, 1, 'test', 'abc')

# Test that the handler is called
print 'Test 4'
codecs.lookup_error('test.lookup')('abc', 0, 1, 'test', 'abc', 'def')

# Test that the handler is called
print 'Test 5'
codecs.lookup_error('test.lookup')('abc', 0, 1, 'test', 'abc', 'def',
