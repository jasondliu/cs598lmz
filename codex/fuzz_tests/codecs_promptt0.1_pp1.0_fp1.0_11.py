import codecs
# Test codecs.register_error

import codecs

def handler(exception):
    print 'handler called'
    return (u'', exception.end)

codecs.register_error('test.lookup', handler)

# Test that the handler is called
print 'Test 1'
print codecs.decode('\xff', 'ascii', 'test.lookup')

# Test that the handler is called
print 'Test 2'
print codecs.decode('\xff', 'ascii', 'test.lookup')

# Test that the handler is called
print 'Test 3'
print codecs.decode('\xff', 'ascii', 'test.lookup')

# Test that the handler is called
print 'Test 4'
print codecs.decode('\xff', 'ascii', 'test.lookup')

# Test that the handler is called
print 'Test 5'
print codecs.decode('\xff', 'ascii', 'test.lookup')

# Test that the handler is called
print 'Test 6'
print codecs.decode
