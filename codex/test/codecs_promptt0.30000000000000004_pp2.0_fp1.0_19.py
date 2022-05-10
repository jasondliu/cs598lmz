import codecs
# Test codecs.register_error

def handler(exception):
    print("handler called", exception)
    return "", exception.end

codecs.register_error("test.lookup", handler)

encoding = "test.lookup"

# Test with a unicode string
s = "abc\u20ac\u20acdef"
