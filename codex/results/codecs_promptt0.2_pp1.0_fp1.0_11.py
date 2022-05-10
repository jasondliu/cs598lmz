import codecs
# Test codecs.register_error()

import codecs

def handler(exception):
    print 'handler:', exception
    return u'\ufffd', exception.end

codecs.register_error('test.lookup', handler)

s = u'\u3042\u3044\u3046\u3048\u304a'
print repr(s.encode('euc-jp', 'test.lookup'))
print repr(s.encode('euc-jp', 'test.lookup'))
print repr(s.encode('euc-jp', 'test.lookup'))
print repr(s.encode('euc-jp', 'test.lookup'))
print repr(s.encode('euc-jp', 'test.lookup'))
print repr(s.encode('euc-jp', 'test.lookup'))
print repr(s.encode('euc-jp', 'test.lookup'))
print repr(s.encode('euc-jp', 'test.lookup'))
print repr(s.encode('
