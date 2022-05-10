import codecs
# Test codecs.register_error

def handler(exception):
    print 'handler called'
    return (u'', exception.end)

codecs.register_error('test.myhandler', handler)

# Test that the handler is called
print '%s' % '\xff'.decode('ascii', 'test.myhandler')

# Test that the handler is called with the correct exception
try:
    '\xff'.decode('ascii', 'test.myhandler')
except UnicodeDecodeError, e:
    print '%s:%s' % (e.__class__.__name__, e.reason)

# Test that the handler is called with the correct exception
try:
    '\xff'.decode('ascii', 'test.myhandler')
except UnicodeDecodeError, e:
    print '%s:%s' % (e.__class__.__name__, e.reason)

# Test that the handler is called with the correct exception
try:
    '\xff'.decode('ascii', 'test.myhandler')
except UnicodeDec
