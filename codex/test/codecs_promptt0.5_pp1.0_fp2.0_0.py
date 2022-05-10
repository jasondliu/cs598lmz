import codecs
# Test codecs.register_error

def handler(exception):
    return ("", exception.end)

codecs.register_error("test.xmlcharrefreplace", handler)

# '\u1234' cannot be encoded as latin-1
s = 'a\u1234b\u1234c'

# With xmlcharrefreplace, the unencodable character is replaced with &#nnn;
# Without, the unencodable character raises an exception
