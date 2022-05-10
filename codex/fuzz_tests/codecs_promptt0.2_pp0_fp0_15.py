import codecs
# Test codecs.register_error

import codecs

def raise_exc(exc):
    raise exc

def test(encoding):
    print '-'*50
    print 'Encoding:', encoding
    print '-'*50
    print 'Registering strict'
    codecs.register_error(encoding, raise_exc)
    print 'Registering ignore'
    codecs.register_error(encoding, 'ignore')
    print 'Registering replace'
    codecs.register_error(encoding, 'replace')
    print 'Registering xmlcharrefreplace'
    codecs.register_error(encoding, 'xmlcharrefreplace')
    print 'Registering backslashreplace'
    codecs.register_error(encoding, 'backslashreplace')
    print 'Registering namereplace'
    codecs.register_error(encoding, 'namereplace')
    print 'Registering backslashreplace'
    codecs.register_error(encoding, 'backslashreplace')
    print 'Registering strict'
    codecs.register_error(encoding, raise_exc)
