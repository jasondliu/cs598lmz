import codecs
# Test codecs.register_error()

import codecs

def handler(exception):
    return ("", exception.end)

def search_function(encoding):
    if encoding == "test.notfound":
        return None, None
    if encoding == "test.errorhandler":
        return codecs.lookup("ascii"), handler
    if encoding == "test.incrementalencoder":
        return codecs.lookup("ascii"), None
    if encoding == "test.incrementaldecoder":
        return codecs.lookup("ascii"), None
    if encoding == "test.streamwriter":
        return codecs.lookup("ascii"), None
    if encoding == "test.streamreader":
        return codecs.lookup("ascii"), None
    return None

codecs.register(search_function)

# Test the search function
for encoding in ["test.notfound", "test.errorhandler",
                 "test.incrementalencoder", "test.incrementaldecoder",
                 "test.streamwriter", "test.streamreader"]:
   
