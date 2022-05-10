import codecs
# Test codecs.register_error()

import codecs

def handler(exception):
    print 'Handling %s' % exception.__class__.__name__
    return (u'', exception.end)

codecs.register_error('test.ignore', handler)
codecs.register_error('test.replace', handler)
codecs.register_error('test.xmlcharrefreplace', handler)
codecs.register_error('test.backslashreplace', handler)

for encoding in ['ascii', 'latin-1', 'utf-8']:
    print 'Encoding:', encoding
    for error in ['strict', 'ignore', 'replace', 'xmlcharrefreplace', 'backslashreplace']:
        print 'Error:', error
        print codecs.decode('\xff', encoding, error)
        print codecs.encode('\u1234', encoding, error)
        print codecs.decode('\xff', encoding, 'test.' + error)
        print codecs.encode('\u1234', encoding, 'test.' + error)

