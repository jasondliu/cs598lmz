import codecs
# Test codecs.register_error

import codecs

def my_error_handler(exception):
    print "my_error_handler:", exception.__class__
    return (u'', exception.end)

codecs.register_error("my_error", my_error_handler)

def test(encoding):
    print "Trying '%s':" % encoding
    try:
        u = unicode("abc\x80\xff", encoding, "my_error")
    except UnicodeError, e:
        print "UnicodeError:", e
    else:
        print "u =", repr(u)

for encoding in ("ascii", "latin-1", "utf-8"):
    test(encoding)

# Test codecs.register_error with a function
# that returns a tuple with a unicode string and an integer

def my_error_handler(exception):
    print "my_error_handler:", exception.__class__
    return (u'\ufffd', exception.end)

codecs.register_error("my_error
