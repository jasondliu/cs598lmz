import codecs
# Test codecs.register_error

import codecs

def my_error_handler(exception):
    print 'my_error_handler called'
    return (u'', exception.end)

codecs.register_error('test.myerrorhandler', my_error_handler)

for encoding in ['ascii', 'latin-1', 'utf-8']:
    print 'Encoding:', encoding
    print repr(unicode('\xff', encoding, 'test.myerrorhandler'))
    print repr(unicode('\xff', encoding, 'ignore'))
    print repr(unicode('\xff', encoding, 'replace'))
    print repr(unicode('\xff', encoding, 'xmlcharrefreplace'))
    print repr(unicode('\xff', encoding, 'strict'))
    print
