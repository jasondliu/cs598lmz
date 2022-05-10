import codecs
# Test codecs.register_error()

import codecs

def handler(exception):
    print 'failed:', exception
    return u'', exception.end

codecs.register_error('test', handler)

for encoding in ['ascii', 'iso8859-1', 'iso8859-2', 'utf-8', 'utf-16']:
    print encoding,
    try:
        print codecs.getdecoder(encoding)('\xff')
    except UnicodeDecodeError, e:
        print 'UnicodeDecodeError:', e

print '\nTest with surrogateescape error handler'

codecs.register_error('test', 'surrogateescape')

for encoding in ['ascii', 'iso8859-1', 'iso8859-2', 'utf-8', 'utf-16']:
    print encoding,
    try:
        print codecs.getdecoder(encoding)('\xff')
    except UnicodeDecodeError, e:
        print 'UnicodeDecodeError:', e
