import codecs
# Test codecs.register_error()

import codecs

def my_error(exception):
    print 'my_error:', exception
    return (u'', exception.end)

codecs.register_error('test.myerror', my_error)

for encoding in ['ascii', 'latin-1', 'utf-8']:
    print 'Encoding:', encoding
    print repr(unicode('abc\xff', encoding, 'test.myerror'))
    print repr(unicode('abc\xff', encoding, 'ignore'))
    print repr(unicode('abc\xff', encoding, 'replace'))
    print repr(unicode('abc\xff', encoding, 'xmlcharrefreplace'))
    print repr(unicode('abc\xff', encoding, 'backslashreplace'))
    print repr(unicode('abc\xff', encoding, 'namereplace'))
    print
