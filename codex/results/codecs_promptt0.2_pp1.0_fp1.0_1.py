import codecs
# Test codecs.register_error

def handler(exception):
    print("handler called")
    return ("?", exception.end)

codecs.register_error("test.lookup", handler)

# Test a lookup error
print(codecs.decode("abc\x80def", "ascii", "test.lookup"))

# Test a cache error
print(codecs.decode("abc\x80def", "ascii", "test.lookup"))

# Test a cache error with replace error handler
print(codecs.decode("abc\x80def", "ascii", "replace"))

# Test a cache error with ignore error handler
print(codecs.decode("abc\x80def", "ascii", "ignore"))

# Test a cache error with xmlcharrefreplace error handler
print(codecs.decode("abc\x80def", "ascii", "xmlcharrefreplace"))

# Test a cache error with backslashreplace error handler
print(codecs.decode("abc\x80def", "ascii",
