import codecs
# Test codecs.register_error

import codecs

def handler(exception):
    print "handler called"
    return (u"", exception.end)

codecs.register_error("test.strict", handler)

# test the basic functionality
print "1.", repr(unicode("abc\u1234", "ascii", "test.strict"))

# test the start parameter
print "2.", repr(unicode("abc\u1234", "ascii", "test.strict", 1))

# test the start parameter
print "3.", repr(unicode("abc\u1234", "ascii", "test.strict", 2))

# test the start parameter
print "4.", repr(unicode("abc\u1234", "ascii", "test.strict", 3))

# test the start parameter
print "5.", repr(unicode("abc\u1234", "ascii", "test.strict", 4))

# test the start parameter
print "6.", repr(unicode("abc\u1234", "ascii", "
