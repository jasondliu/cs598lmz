import codecs
# Test codecs.register_error()
# This test is for the Python 3 case.  Python 2 uses a different
# mechanism for codec error handling.

import codecs

def handler(err):
    print(err)
    return u"", err.start + 1

codecs.register_error("test.strict", handler)

s = "x\x80y\xe0\x80z"

