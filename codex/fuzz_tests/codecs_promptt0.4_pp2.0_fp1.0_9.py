import codecs
# Test codecs.register_error
# See http://bugs.python.org/issue1756

def test_register_error():
    # Test that codecs.register_error() works with non-standard error handlers
    # (see http://bugs.python.org/issue1756)
    import codecs
    import encodings.utf_8

    class MyError(UnicodeError):
        pass

    class MyHandler(object):
        def __init__(self, errors='strict'):
            self.errors = errors

        def __call__(self, exception):
            if not isinstance(exception, UnicodeError):
                raise TypeError("don't know how to handle %r" % exception)
            print 'MyHandler called with %r' % exception
            return (u'', exception.end)

    codecs.register_error('test.myerror', MyHandler)

    # First, test that the default error handler for UTF-8 is 'strict'
    # (see http://bugs.python.org/issue1756#msg121282)
    try:
        encodings.utf_
