import codecs
codecs.register_error('multibytecodec_error', codecs.multibytecodec_error)

#
# Test pretty printing
#

def test_pprint():
    if not hasattr(sys, 'pypy_version_info'):
        import _tkinter
    else:
        sys.modules['_tkinter'] = None
    import _socket
    import _ssl
    import _hashlib
    import _random
    import __main__
    import __phello__
    import _warnings
    import _weakref
    import _abc

    pprint.pprint([_tkinter, _socket, _ssl, _hashlib, _random, __main__,
                    __phello__, _warnings, _weakref, _abc])

def test_saferepr():
    class X(object):
        def __init__(self, a):
            self.a = a
        def __repr__(self):
            return 'X(%s,%s)' % (self.a, self.b)
    S_53bits = '%s%
