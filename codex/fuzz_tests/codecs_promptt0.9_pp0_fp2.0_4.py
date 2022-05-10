import codecs
# Test codecs.register_error
# Currently this is only supported in PyVarObject_FromSize, PyLong_FromLong,
# and PyUnicode_FromUnicode.

def my_error_func(exc):
    #print "exc = ", exc
    if isinstance(exc, UnicodeEncodeError):
        #print "ucstest: error '%s' for %s at %s" % (
        #    exc.__class__.__name__,
        #    str(exc.object[exc.start/2:exc.end/2]),
        #    exc.start/2)
        s = exc.object[exc.start/2:exc.end/2]
        n = len(s)
        return str(n), exc.start/2+n
    elif isinstance(exc, UnicodeDecodeError):
        #print "ucstest: error '%s' for '%s' at %s" % (
        #    exc.__class__.__name__,
        #    str(chr(exc.object[exc.start])),
        #    exc.
