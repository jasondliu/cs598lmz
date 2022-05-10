import codecs
# Test codecs.register_error

# encoding.py uses this error handler to re-encode iso-8859-1 as utf-8
def reencode_iso8859_1(exc):
    print "hello"
    if not isinstance(exc, UnicodeEncodeError) or exc.encoding != "iso-8859-1":
        raise TypeError("don't know how to handle %r in error callback" % exc)
    print "callback called"
    print "object=%s" % exc.object
    print "start=%s" % exc.start
    print "end=%s" % exc.end
    print "reason=%s" % exc.reason
    object = unicode(exc.object, encoding="iso-8859-1")
    return (object.encode("utf-8"), exc.end)

def test(name, encoding):
    try:
        "my name is %s" % name
    except:
        print "ERROR", name
    print "after error"
    return codecs.charmap_encode(name, encoding)[0]

def
