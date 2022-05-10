import codecs
# Test codecs.register_error

def handler(exception):
    print("handler called")
    return ("?", exception.end)

codecs.register_error("test.lookup", handler)

# Test that the handler is called
print(codecs.lookup_error("test.lookup"))

# Test that the handler is called
print(codecs.lookup_error("test.lookup"))

# Test that the handler is called
print(codecs.lookup_error("test.lookup"))

# Test that the handler is called
print(codecs.lookup_error("test.lookup"))

# Test that the handler is called
print(codecs.lookup_error("test.lookup"))

# Test that the handler is called
print(codecs.lookup_error("test.lookup"))

# Test that the handler is called
print(codecs.lookup_error("test.lookup"))

# Test that the handler is called
print(codecs.lookup_error("test.lookup"))

# Test that the
