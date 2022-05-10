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
