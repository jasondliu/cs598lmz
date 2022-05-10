import codecs
# Test codecs.register_error

import codecs

def my_error_handler(exception):
    print "my_error_handler:", exception
    return (u'', exception.end)

codecs.register_error("test.my_error_handler", my_error_handler)

def test(encoding):
    print encoding
    print codecs.lookup_error("test.my_error_handler")
    print codecs.lookup_error("test.my_error_handler") is my_error_handler
    print codecs.lookup_error("test.my_error_handler") is codecs.lookup_error("test.my_error_handler")
    print codecs.lookup_error("test.my_error_handler") is codecs.lookup_error("test.my_error_handler")
    print codecs.lookup_error("test.my_error_handler") is codecs.lookup_error("test.my_error_handler")
    print codecs.lookup_error("test.my_error_handler") is codecs.lookup_error
