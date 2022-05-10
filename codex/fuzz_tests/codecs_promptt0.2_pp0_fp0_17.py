import codecs
# Test codecs.register_error

def handler(exception):
    print("handler called")
    return ("?", exception.end)

codecs.register_error("test.strict", handler)

print(codecs.decode("abc\ud800", "ascii", "test.strict"))
print(codecs.decode("abc\ud800", "ascii", "test.strict"))
print(codecs.decode("abc\ud800", "ascii", "test.strict"))
print(codecs.decode("abc\ud800", "ascii", "test.strict"))
print(codecs.decode("abc\ud800", "ascii", "test.strict"))
print(codecs.decode("abc\ud800", "ascii", "test.strict"))
print(codecs.decode("abc\ud800", "ascii", "test.strict"))
print(codecs.decode("abc\ud800", "ascii", "test.strict"))
print(codec
