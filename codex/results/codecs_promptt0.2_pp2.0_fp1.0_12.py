import codecs
# Test codecs.register_error

# This test is for the case where the error handler is not a string
# and does not have a name attribute.

class MyError(Exception):
    def __init__(self, encoding, reason):
        self.encoding = encoding
        self.reason = reason

def my_handler(exception):
    if isinstance(exception, MyError):
        print('my_handler called for %s' % exception.reason)
        return ('', exception.start + 1)
    else:
        raise TypeError("don't know how to handle %r" % exception)

codecs.register_error("test.my_handler", my_handler)

def search_function(encoding):
    if encoding == "test.my_handler":
        return codecs.lookup("utf-8")

codecs.register(search_function)

# Encode
encoder = codecs.getencoder("test.my_handler")
(output, consumed) = encoder("abc\u1234def")
print(repr(output))
print(consumed)
