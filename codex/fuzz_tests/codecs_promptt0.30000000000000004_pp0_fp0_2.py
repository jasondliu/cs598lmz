import codecs
# Test codecs.register_error()

def handler(exception):
    return (u'\ufffd', exception.end)

codecs.register_error("test.xmlcharrefreplace", handler)

# Test that the error handler is called
for input, expected in [
    (u"\u0100", u"\ufffd"),
    (u"\u0100\u0100", u"\ufffd\ufffd"),
    (u"\u0100\u0100\u0100", u"\ufffd\ufffd\ufffd"),
    (u"\u0100\u0100\u0100\u0100", u"\ufffd\ufffd\ufffd\ufffd"),
    (u"\u0100\u0100\u0100\u0100\u0100", u"\ufffd\ufffd\ufffd\ufffd\ufffd"),
    (u"\u0100\u0100\u0100\u0100\u0100\u0100", u"\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd"),
    (u"\u0100\u0100\u0100\u
