import codecs
# Test codecs.register_error()

import codecs

def handler(exception):
    print 'Error:', exception
    return (u'', exception.end)

codecs.register_error('test.myerror', handler)

for encoding in ['ascii', 'latin1', 'iso-8859-1', 'iso-8859-15']:
    print '\nTesting encoding:', encoding
    print '-' * 30
    text = u'pi: \u03c0'
    print 'TEXT:', repr(text)
    print 'ENCODED:', codecs.encode(text, encoding, 'test.myerror')

# Test codecs.lookup_error()

import codecs

def handler(exception):
    print 'Error:', exception
    return (u'', exception.end)

codecs.register_error('test.myerror', handler)

for encoding in ['ascii', 'latin1', 'iso-8859-1', 'iso-8859-15']:
    print '\nTesting encoding:', encoding

