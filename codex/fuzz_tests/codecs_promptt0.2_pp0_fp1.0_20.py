import codecs
# Test codecs.register_error

import codecs

def my_error_handler(exception):
    return (u'', exception.end)

codecs.register_error('my_error', my_error_handler)

def test(encoding):
    print '-'*20, encoding, '-'*20
    print codecs.decode('\xff', encoding, 'strict')
    print codecs.decode('\xff', encoding, 'replace')
    print codecs.decode('\xff', encoding, 'ignore')
    print codecs.decode('\xff', encoding, 'xmlcharrefreplace')
    print codecs.decode('\xff', encoding, 'backslashreplace')
    print codecs.decode('\xff', encoding, 'namereplace')
    print codecs.decode('\xff', encoding, 'my_error')

for encoding in ['latin-1', 'ascii', 'utf-8']:
    test(encoding)
