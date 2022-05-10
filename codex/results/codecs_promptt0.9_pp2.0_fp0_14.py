import codecs
# Test codecs.register_error('test', test_error)
def test_register_error(errcls):
    # First unregister the error class, to silence the duplicate registration
    # warning
    import codecs
    codecs.register_error('test', errcls)
    s = '123\ud800\ud800\ud800456\ud800\ud800\ud800'
    u = codecs.encode(s, 'iso8859-1', 'test')
    if hasattr(u, "__len__"):
        u = u.decode('iso8859-1')
    assert u == '123\uFFFD\uFFFD\uFFFD456\uFFFD\uFFFD\uFFFD'
    s2 = codecs.decode(u, 'iso8859-1', 'test')
    assert s2 == s

class register_error_UnicodeSUBError(UnicodeEncodeError):
    def __init__(self, obj):
        self.start = 0
        self.end = 0
        UnicodeEncodeError.__init__(
