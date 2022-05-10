import codecs
# Test codecs.register_error()

def handler(exception):
    return (u'', exception.end)

codecs.register_error('test', handler)

def test(encoding):
    print '%s:' % encoding,
    try:
        unicode('abc\x80def', encoding, 'test')
    except UnicodeDecodeError, detail:
        print 'UnicodeDecodeError:', detail
    else:
        print 'no exception'

for encoding in ['ascii', 'latin-1', 'utf-8']:
    test(encoding)

print 'Done'
