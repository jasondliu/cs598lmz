import codecs
# Test codecs.register_error

def search_function(encoding):
    if encoding == "test.unicode":
        return codecs.lookup("utf-8")
    return None

codecs.register(search_function)

