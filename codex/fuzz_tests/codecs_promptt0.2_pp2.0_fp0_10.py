import codecs
# Test codecs.register_error

import codecs

def handler(exception):
    print "handler called"
    return (u"\ufffd", exception.end)

codecs.register_error("test.myhandler", handler)

# test with a builtin codec
s = u"abc\u1234def"
try:
    s.encode("ascii")
except UnicodeEncodeError, e:
    print "UnicodeEncodeError"
    print e.encoding
    print e.object
    print e.start
    print e.end
    print e.reason
    print e.message
    print e.args
    print repr(str(e))

print "---"

# test with a lookup codec
s = u"abc\u1234def"
try:
    s.encode("test.mylookup")
except UnicodeEncodeError, e:
    print "UnicodeEncodeError"
    print e.encoding
    print e.object
    print e.start
    print e.end
    print e.reason
    print e
