import codecs
# Test codecs.register_error

def handler(exception):
    return ('', exception.end)

codecs.register_error('test.strict', handler)
codecs.register_error('test.ignore', handler)
codecs.register_error('test.replace', handler)
codecs.register_error('test.xmlcharrefreplace', handler)
codecs.register_error('test.backslashreplace', handler)

def test(encoding):
    print '-'*50
    print 'Encoding', encoding
    print '-'*50
    print 'DEFAULT'
    print '-'*50
    print '\xe4'.decode(encoding)
    print '-'*50
    print 'STRICT'
    print '-'*50
    print '\xe4'.decode(encoding, 'strict')
    print '-'*50
    print 'IGNORE'
    print '-'*50
    print '\xe4'.decode(encoding, 'ignore')
    print '-'*50
    print 'REPLACE'
    print '-'
