import codecs
# Test codecs.register_error

import codecs

def my_error_handler(exception):
    print "my_error_handler: %r" % exception
    return (u"\ufffd", exception.end)

codecs.register_error("test.my_error_handler", my_error_handler)

# Test the error handler
encoding = "ascii"

for input, expected in [
    (u"abc\u1234", u"abc\ufffd"),
    (u"abc\u1234\u1234", u"abc\ufffd\ufffd"),
    (u"abc\u1234\u1234\u1234", u"abc\ufffd\ufffd\ufffd"),
    (u"abc\u1234\u1234\u1234\u1234", u"abc\ufffd\ufffd\ufffd\ufffd"),
    (u"abc\u1234\u1234\u1234\u1234\u1234", u"abc\ufffd\ufffd\ufffd\ufffd\ufffd"),

