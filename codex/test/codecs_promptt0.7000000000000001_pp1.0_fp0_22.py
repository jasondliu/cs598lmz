import codecs
# Test codecs.register_error

import codecs
import string

def searchFunc(encoding):
    if encoding == "test":
        return codecs.lookup("ascii")
    return None

# Use str.encode() as our errorhandler
def bad(msg):
    raise UnicodeError(msg)

codecs.register_error("test.bad", bad)

# test normal codec lookup

for encoding in ["utf-8", "ascii"]:
    for errors in [None, "strict", "ignore", "replace"]:
        print("Normal lookup: %s, %s" % (encoding, errors))
