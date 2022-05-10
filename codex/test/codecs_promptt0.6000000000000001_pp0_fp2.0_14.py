import codecs
# Test codecs.register_error()

# Test codecs.register_error()

import codecs
import sys

def handler(exception):
    return (u"", exception.end)

codecs.register_error("test.my_error", handler)

enc = codecs.getencoder("utf-8")

