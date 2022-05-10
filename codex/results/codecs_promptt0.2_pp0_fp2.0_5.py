import codecs
# Test codecs.register_error

import codecs

def my_error_handler(exception):
    return (u'', exception.end)

codecs.register_error('my_error', my_error_handler)

def test(encoding):
    print '-'*20, encoding, '-'*20
    try:
        print codecs.decode('\xff', encoding, 'strict')
    except UnicodeDecodeError, e:
        print 'UnicodeDecodeError:', e
    print codecs.decode('\xff', encoding, 'my_error')
    print codecs.decode('\xff', encoding, 'replace')
    print codecs.decode('\xff', encoding, 'ignore')

for encoding in ['ascii', 'latin-1', 'utf-8']:
    test(encoding)
