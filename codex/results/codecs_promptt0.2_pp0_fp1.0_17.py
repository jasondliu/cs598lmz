import codecs
# Test codecs.register_error()

import codecs

def handler(exception):
    print 'handler:', exception
    return '\x00', exception.end

codecs.register_error('test.lookup', handler)

def test(encoding):
    print '-' * 50
    print encoding
    print '-' * 50
    print 'DEFAULT'.ljust(20), repr(unicode('abc\u1234', encoding))
    print 'IGNORE'.ljust(20), repr(unicode('abc\u1234', encoding, 'ignore'))
    print 'REPLACE'.ljust(20), repr(unicode('abc\u1234', encoding, 'replace'))
    print 'BACKSLASHREPLACE'.ljust(20), repr(unicode('abc\u1234', encoding, 'backslashreplace'))
    print 'XMLCHARREFREPLACE'.ljust(20), repr(unicode('abc\u1234', encoding, 'xmlcharrefreplace'))
    print 'TEST.LOOKUP'.ljust(20), repr(unicode('abc
