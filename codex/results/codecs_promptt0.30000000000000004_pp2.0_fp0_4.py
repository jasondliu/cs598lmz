import codecs
# Test codecs.register_error

def handler(exception):
    print("handler called")
    return (u"\ufffd", exception.end)

codecs.register_error("test.lookup", handler)

print(codecs.lookup_error("test.lookup"))

# Test codecs.lookup_error

print(codecs.lookup_error("test.lookup"))

# Test codecs.lookup_error

print(codecs.lookup_error("test.lookup"))

# Test codecs.lookup_error

print(codecs.lookup_error("test.lookup"))

# Test codecs.lookup_error

print(codecs.lookup_error("test.lookup"))

# Test codecs.lookup_error

print(codecs.lookup_error("test.lookup"))

# Test codecs.lookup_error

print(codecs.lookup_error("test.lookup"))

# Test codecs.lookup_error

print(codec
