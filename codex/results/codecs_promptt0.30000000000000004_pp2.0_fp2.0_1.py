import codecs
# Test codecs.register_error

def handler(exception):
    return (u"", exception.end)

codecs.register_error('test.xmlcharrefreplace', handler)

# Test that the error handler is called
u"\u1234".encode("ascii", "test.xmlcharrefreplace")

# Test that the error handler is not called
u"\u1234".encode("ascii", "xmlcharrefreplace")

# Test that the error handler is called
u"\u1234".encode("ascii", "test.xmlcharrefreplace")

# Test that the error handler is not called
u"\u1234".encode("ascii", "xmlcharrefreplace")

# Test that the error handler is called
u"\u1234".encode("ascii", "test.xmlcharrefreplace")

# Test that the error handler is not called
u"\u1234".encode("ascii", "xmlcharrefreplace")

# Test that the error handler is called
u"\u1234".encode("as
