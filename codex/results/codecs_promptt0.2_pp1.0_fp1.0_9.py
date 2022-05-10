import codecs
# Test codecs.register_error

import codecs

def my_error(exception):
    return ("my_error", exception.end)

codecs.register_error("my_error", my_error)

def test(encoding):
    print '-'*20, encoding, '-'*20
    try:
        u = unicode("abc\x80\xff", encoding, "my_error")
    except UnicodeError, e:
        print 'UnicodeError:', e.__class__, e
    else:
        print repr(u)

for encoding in ["ascii", "latin-1", "utf-8", "utf-16"]:
    test(encoding)

# Test codecs.register_error with a function that returns a tuple

def my_error_tuple(exception):
    return ("my_error_tuple", exception.end)

codecs.register_error("my_error_tuple", my_error_tuple)

def test(encoding):
    print '-'*20, encoding, '-'*20
   
