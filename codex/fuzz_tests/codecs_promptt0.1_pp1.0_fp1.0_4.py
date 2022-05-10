import codecs
# Test codecs.register_error()

import codecs

def my_error_handler(exception):
    print 'my_error_handler:', exception
    return (u'', exception.end)

codecs.register_error('test.myerrorhandler', my_error_handler)

for encoding in ['ascii', 'latin-1', 'utf-8']:
    print 'Encoding:', encoding
    print '  u"abc"   :', codecs.decode(u'abc', encoding, 'test.myerrorhandler')
    print '  u"\xff"  :', codecs.decode(u'\xff', encoding, 'test.myerrorhandler')
    print '  u"\u0100":', codecs.decode(u'\u0100', encoding, 'test.myerrorhandler')
    print '  u"\u8123":', codecs.decode(u'\u8123', encoding, 'test.myerrorhandler')
    print '  u"\udcba":', codecs.decode(u'\udcba', encoding, '
