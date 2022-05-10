import codecs
# Test codecs.register_error

def search_function(encoding):
    if encoding == "test.unicode.notfound":
        return codecs.lookup(encoding)
    else:
        return None

codecs.register_error("test.notfound", search_function)

