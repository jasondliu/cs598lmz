import codecs
# Test codecs.register_error().

def handler(exception):
    return ("code: %d" % exception.start, exception.end)

codecs.register_error("test.myencodeerrorhandler", handler)
codecs.register_error("test.mydecodeerrorhandler", handler)

try:
    codecs.encode("abc\xe0", "ascii", "test.myencodeerrorhandler")
except Exception, e:
    print "ERROR:", e
else:
    print "OK"

try:
    codecs.decode("abc\xe0", "ascii", "test.mydecodeerrorhandler")
except Exception, e:
    print "ERROR:", e
else:
    print "OK"

try:
    codecs.encode("abc\xe0", "ascii", "test.unknown")
except Exception, e:
    print "ERROR:", e
else:
    print "OK"

try:
    codecs.decode("abc\xe0", "ascii", "test.unknown")
except Exception,
