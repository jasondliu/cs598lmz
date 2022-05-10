import codecs
# Test codecs.register_error

import codecs

def my_error_handler(exception):
    print "my_error_handler:", exception
    return (u'', exception.end)

def test():
    codecs.register_error("test.my_error_handler", my_error_handler)
    s = u'\udc00'
    print repr(s.encode("ascii", "test.my_error_handler"))

test()
