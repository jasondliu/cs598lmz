import codecs
# Test codecs.register_error.

import codecs

def handler(exception):
    return (u"\ufffd", exception.end)

codecs.register_error("test.xmlcharrefreplace", handler)

