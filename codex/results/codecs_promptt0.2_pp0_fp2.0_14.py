import codecs
# Test codecs.register_error()

import codecs

def handler(exception):
    print "handler called"
    return (u"\ufffd", exception.end)

codecs.register_error("test.xmlcharrefreplace", handler)

print "XMLCHARREFREPLACE"
print repr(u"abc\u1234\u12345".encode("ascii", "xmlcharrefreplace"))
print repr(u"abc\u1234\u12345".encode("ascii", "test.xmlcharrefreplace"))

print "IGNORE"
print repr(u"abc\u1234\u12345".encode("ascii", "ignore"))
print repr(u"abc\u1234\u12345".encode("ascii", "test.ignore"))

print "REPLACE"
print repr(u"abc\u1234\u12345".encode("ascii", "replace"))
print repr(u"abc\u1234\u12345".encode("ascii", "test.replace"))

print "BACKSL
