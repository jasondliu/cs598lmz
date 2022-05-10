import codecs
# Test codecs.register_error:

def handler1(exception):
    return ('/', exception.end)

def handler2(exception):
    return ('/', 1)

print u'Test 1'
print codecs.escape_encode(u'\udc00\ud801\udc00\ud801')[0]

print u'Test 2'
codecs.register_error('test.lookup', handler1)
print codecs.escape_encode(u'\udc00\ud801\udc00\ud801',
                          'test.lookup')[0]

print u'Test 3'
codecs.register_error('test.lookup', handler2)
print codecs.escape_encode(u'\udc00\ud801\udc00\ud801',
                          'test.lookup')[0]

# Test codecs.register_error:

print u'Test 4'
codecs.register_error('test.strict', codecs.ignore_errors)
print codecs.escape_decode(
   
