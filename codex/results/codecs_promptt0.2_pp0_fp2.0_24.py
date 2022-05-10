import codecs
# Test codecs.register_error

def handler(exception):
    print("handler called")
    return (u"\ufffd", exception.end)

codecs.register_error("test.myhandler", handler)

# Test that the handler is called
print(codecs.decode("abc\xffdef", "ascii", "test.myhandler"))

# Test that the handler is called for a UnicodeEncodeError
print(codecs.encode("abc\udcffdef", "ascii", "test.myhandler"))

# Test that the handler is called for a UnicodeTranslateError
print(codecs.encode("abc\udcffdef", "ascii", "test.myhandler", "strict"))

# Test that the handler is called for a UnicodeDecodeError
print(codecs.decode("abc\xffdef", "ascii", "test.myhandler", "strict"))

# Test that the handler is called for a UnicodeDecodeError
print(codecs.decode("abc\xffdef", "ascii", "test.my
