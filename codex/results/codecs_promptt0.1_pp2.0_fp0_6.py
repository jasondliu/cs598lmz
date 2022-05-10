import codecs
# Test codecs.register_error

import codecs

def my_error_handler(exception):
    print "my_error_handler called"
    return (u'', exception.end)

codecs.register_error("test.my_error_handler", my_error_handler)

def test(encoding):
    print "testing", encoding
    try:
        u"abc\u1234".encode(encoding, "test.my_error_handler")
    except UnicodeEncodeError, e:
        print "UnicodeEncodeError:", e

for encoding in ["ascii", "latin-1", "utf-8"]:
    test(encoding)

# Test codecs.register_error with a function that returns a tuple

def my_error_handler(exception):
    print "my_error_handler called"
    return (u'', exception.end)

codecs.register_error("test.my_error_handler", my_error_handler)

def test(encoding):
    print "testing", encoding
    try:
       
