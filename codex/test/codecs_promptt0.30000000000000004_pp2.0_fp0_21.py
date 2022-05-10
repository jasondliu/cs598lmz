import codecs
# Test codecs.register_error

import codecs

def handler(exception):
    return ("", exception.end)

codecs.register_error("test.lookup", handler)

