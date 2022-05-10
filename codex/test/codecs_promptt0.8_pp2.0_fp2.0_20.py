import codecs
# Test codecs.register_error()

import sys
try:
    str.encode
except AttributeError:
    # Python 2
    bytes = str
    byte = chr
else:
    # Python 3
    bytes = bytes
    byte = bytes

