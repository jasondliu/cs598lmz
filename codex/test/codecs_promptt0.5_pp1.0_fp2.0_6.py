import codecs
# Test codecs.register_error()

def handler(exception):
    print("Ignoring exception:", exception)
    return (" ", exception.start + 1)

codecs.register_error("test.ignore", handler)

# Encode the string without ignoring the error
