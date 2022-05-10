import codecs
# Test codecs.register_error()
def search_function(encoding):
    if encoding == "test.unicode":
        return codecs.codec_search_function("utf-16-le")

codecs.register(search_function)

# Test codecs.lookup()
def search_function(encoding):
    if encoding == "test.unicode":
        return codecs.lookup("utf-16-le")

# Test codecs.lookup_error()
def search_function(encoding):
    if encoding == "test.unicode":
        return codecs.lookup_error("ignore")

# Test codecs.StreamReader()
def search_function(encoding):
    if encoding == "test.unicode":
        return codecs.StreamReader(codecs.getreader("utf-16-le"))

def search_function(encoding):
    if encoding == "test.unicode":
        return codecs.StreamReader(codecs.getreader("utf-16-le"), "strict")

