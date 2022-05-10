import codecs
# Test codecs.register_error

def handler(exception):
    print "handler called"
    return u"", exception.end

codecs.register_error("test.lookup", handler)

try:
    u"\x80".encode("ascii", "test.lookup")
except UnicodeEncodeError, x:
    print x

codecs.register_error("test.strict", codecs.strict_errors)

try:
    u"\x80".encode("ascii", "test.strict")
except UnicodeEncodeError, x:
    print x

codecs.register_error("test.replace", codecs.replace_errors)

print u"\x80".encode("ascii", "test.replace")

codecs.register_error("test.ignore", codecs.ignore_errors)

print u"\x80".encode("ascii", "test.ignore")
