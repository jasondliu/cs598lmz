import codecs
# Test codecs.register_error()

import codecs

def handler(exception):
    print 'Exception:', exception
    return u'\ufffd', exception.end

codecs.register_error('test.myerrorhandler', handler)

for encoding in ['ascii', 'latin-1', 'utf-8']:
    print 'Encoding:', encoding
    print repr(unicode('abc\x80def', encoding, 'test.myerrorhandler'))
    print repr(unicode('abc\x80def', encoding, 'ignore'))
    print repr(unicode('abc\x80def', encoding, 'replace'))
    print repr(unicode('abc\x80def', encoding, 'xmlcharrefreplace'))
    print repr(unicode('abc\x80def', encoding, 'strict'))
    print
