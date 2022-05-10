import codecs
# Test codecs.register_error()

import codecs

def my_error_handler(exception):
    print 'my_error_handler:', exception
    return (u'', exception.end)

codecs.register_error('test.strict', my_error_handler)

for encoding in ['test.strict', 'test.strict', 'test.strict']:
    print 'ENCODING:', encoding
    print codecs.decode('\xff', encoding)
    print codecs.decode('\xff', encoding, 'replace')
    print codecs.decode('\xff', encoding, 'ignore')
    print codecs.decode('\xff', encoding, 'xmlcharrefreplace')
    print codecs.decode('\xff', encoding, 'backslashreplace')
    print codecs.decode('\xff', encoding, 'namereplace')
    print codecs.decode('\xff', encoding, my_error_handler)
    print codecs.decode('\xff', encoding, 'strict')
    print codecs.decode('\xff', encoding, '
