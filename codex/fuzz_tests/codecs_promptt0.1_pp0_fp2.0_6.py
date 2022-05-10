import codecs
# Test codecs.register_error

import codecs

def handler(exception):
    print "handler called"
    return (u"", exception.end)

codecs.register_error("test.myhandler", handler)

for encoding in ["ascii", "latin-1", "utf-8"]:
    print encoding
    print codecs.decode("abc\xffdef", encoding, "test.myhandler")
    print codecs.decode("abc\xffdef", encoding, "ignore")
    print codecs.decode("abc\xffdef", encoding, "replace")
    print codecs.decode("abc\xffdef", encoding, "xmlcharrefreplace")
    print codecs.decode("abc\xffdef", encoding, "strict")

# Test codecs.lookup

import codecs

def handler(exception):
    print "handler called"
    return (u"", exception.end)

codecs.register_error("test.myhandler", handler)

for encoding in ["ascii", "latin-1", "utf-8"]:
