import codecs
# Test codecs.register_error

def handler(exception):
    return (u'', exception.end)

codecs.register_error('test.ignore', handler)
codecs.register_error('test.replace', handler)
codecs.register_error('test.xmlcharrefreplace', handler)
codecs.register_error('test.backslashreplace', handler)

for encoding in ('ascii', 'latin-1', 'utf-8'):
    print '%s:' % encoding
    for error in ('strict', 'ignore', 'replace', 'xmlcharrefreplace',
                  'backslashreplace'):
        print ' ', error,
        try:
            print codecs.decode(u'\udcff', encoding, error)
        except UnicodeDecodeError, e:
            print 'UnicodeDecodeError'
        try:
            print codecs.encode(u'\udcff', encoding, error)
        except UnicodeEncodeError, e:
            print 'UnicodeEncodeError'
        try:
            print codecs.en
