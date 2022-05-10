import codecs
# Test codecs.register_error
# Issue #4620

def x2a(exc):
    return (u'\\x%02x' % ord(exc.object[exc.start]), exc.end)
codecs.register_error('test_a', x2a)

def x2b(exc):
    return (u'\\x%02x' % ord(exc.object[exc.start]), exc.end)
codecs.register_error('test_b', x2b)



s = '\xff'
u = u'\xff'
for encoding in ('ascii', 'latin-1', 'utf-8'):
    for errors in ('strict', 'ignore', 'replace', 'test_a', 'xmlcharrefreplace', 'test_b'):
        print encoding, errors,
        try:
            r = s.decode(encoding, errors)
            print r == u or repr(r) == repr(u)
        except UnicodeError, e:
            print e.__class__.__name__

print 'Done.'
