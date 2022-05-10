import codecs
# Test codecs.register_error()

import codecs
import encodings

def search_function(encoding):
    if encoding == "test.unicode":
        return codecs.lookup("utf-8")
    return None

codecs.register(search_function)

# Test that the codec is found
