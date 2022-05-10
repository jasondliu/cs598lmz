import codecs
# Test codecs.register_error

import codecs

def my_error_handler(exception):
    print "my_error_handler:", exception
    return (u'', exception.end)

codecs.register_error("test.my_error_handler", my_error_handler)

# Test the error handler
s = u'\u3042\u3044\u3046\u3048\u304a'
print repr(s)
print repr(s.encode("euc-jp", "test.my_error_handler"))
print repr(s.encode("euc-jp", "test.my_error_handler"))
print repr(s.encode("euc-jp", "test.my_error_handler"))
print repr(s.encode("euc-jp", "test.my_error_handler"))
print repr(s.encode("euc-jp", "test.my_error_handler"))
print repr(s.encode("euc-jp", "test.my_error_handler"))
print repr(s.encode("euc-jp",
