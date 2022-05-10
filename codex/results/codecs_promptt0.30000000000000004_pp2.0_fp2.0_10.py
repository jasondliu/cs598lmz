import codecs
# Test codecs.register_error

import codecs

def handler(exception):
    print 'handler called'
    return (u'', exception.end)

codecs.register_error('test.strict', handler)

for encoding in ['ascii', 'latin-1', 'utf-8']:
    print '%r' % encoding
    print codecs.decode('\x80', encoding, 'test.strict')
    print codecs.decode('\x80', encoding, 'test.strict')
    print codecs.decode('\x80', encoding, 'test.strict')
    print codecs.decode('\x80', encoding, 'test.strict')
    print codecs.decode('\x80', encoding, 'test.strict')
    print codecs.decode('\x80', encoding, 'test.strict')
    print codecs.decode('\x80', encoding, 'test.strict')
    print codecs.decode('\x80', encoding, 'test.strict')
    print codecs.decode
