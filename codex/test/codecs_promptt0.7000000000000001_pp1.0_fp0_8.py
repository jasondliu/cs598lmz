import codecs
# Test codecs.register_error(), bug #7832
def u_replace(exc):
    if not isinstance(exc, (UnicodeDecodeError, UnicodeEncodeError)):
        raise TypeError("don't know how to handle %r" % exc)
    return (u'', exc.end)
codecs.register_error('test.u_replace', u_replace)

def test_error_callback():
    # bug #8368: error callback must be able to return a tuple
    u = chr(0xfffd)
    s = '\xff'

    for encoding in ('ascii', 'utf-8', 'latin-1', 'utf-16'):
        for bad, good in ((s, u), (unicode(s), u)):
            assert unicode(bad, encoding, 'test.u_replace') == good
            assert bad.decode(encoding, 'test.u_replace') == good

def test_ignore():
    # bug #8368: error callback must be able to return a tuple
    s = '\xff'

