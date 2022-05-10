import codecs
# Test codecs.register_error()

import codecs
import encodings

# test codecs.register_error()

def search_function(encoding):
    if encoding == "test.unicode":
        return codecs.lookup(encoding)
    return None

codecs.register(search_function)

