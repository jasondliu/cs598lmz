import codecs
# Test codecs.register_error

def handler(exception):
    print "handler called"
    return u"\ufffd", exception.end

codecs.register_error("test.replace", handler)

print "registering handler"

print "testing UnicodeEncodeError handler"
u"\u1111".encode("ascii", "test.replace")

print "testing UnicodeDecodeError handler"
"\xff".decode("ascii", "test.replace")

print "testing UnicodeTranslateError handler"
u"\u1111".translate({0x1111: u"\ufffd"}, "test.replace")

print "testing LookupError handler"
u"\u1111".encode("no-such-encoding", "test.replace")

print "testing TypeError handler"
u"\u1111".encode("ascii", 42)
