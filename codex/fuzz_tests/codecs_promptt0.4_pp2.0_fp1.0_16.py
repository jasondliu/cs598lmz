import codecs
# Test codecs.register_error

def test_register_error(encoding):
    # Check that codecs.register_error() can be called with a unicode
    # error handler name.
    codecs.register_error(encoding, 'ignore')
    codecs.register_error(encoding, 'replace')
    codecs.register_error(encoding, 'xmlcharrefreplace')
    codecs.register_error(encoding, 'backslashreplace')
    codecs.register_error(encoding, 'namereplace')
    codecs.register_error(encoding, 'strict')
    codecs.register_error(encoding, 'surrogateescape')
    codecs.register_error(encoding, 'surrogatepass')
    codecs.register_error(encoding, 'ignore')
    codecs.register_error(encoding, 'replace')
    codecs.register_error(encoding, 'xmlcharrefreplace')
    codecs.register_error(encoding, 'backslashreplace')
    codecs.register_error(encoding, 'namereplace')

