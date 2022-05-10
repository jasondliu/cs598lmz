import codecs
# Test codecs.register_error()

import codecs

def handler(exception):
    return (u"", exception.end)

codecs.register_error("test.ignore", handler)

text = u"\u20ac" + u"\x81" + u"\u20ac"

