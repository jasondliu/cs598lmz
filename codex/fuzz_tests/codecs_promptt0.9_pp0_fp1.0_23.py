import codecs
# Test codecs.register_error
def g1(exc):
    if isinstance(exc, UnicodeEncodeError):
        x, = exc.args
        return (u'&#%d;' % ord(x), 1)
    elif isinstance(exc, UnicodeDecodeError):
        x, = exc.args
        return (unichr(int(x[2:-1])), 1)
    else:
        raise TypeError, "don't know how to handle %r" % exc

codecs.register_error('test.xmlcharrefreplace', g1)

def test_main(verbose=None):
    test_function(verbose)
    test_codec(verbose)

if __name__ == '__main__':
    test_main(verbose=True)
