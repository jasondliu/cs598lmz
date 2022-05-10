import codecs
# Test codecs.register_error() by implementing and installing
# a local module that replaces the "replace" error handler.
# This module is named "strict" because it will raise an
# exception rather than replace bad data.

# This module is valid python code, but it's not compatible
# with Python 3.x (which doesn't know about codec classes).

# In addition to registering the error handler, the module
# also creates a local codec, "strict_utf8".  The codec is
# an exact copy of "utf-8", except it doesn't use the
# "ignore" or "replace" error handlers.  Instead, it uses
# the "strict" error handler defined in the same module.

# --- begin strict.py ---

#import codecs
import encodings
from encodings import utf_8

# Python 2.x only
#class StrictReplace(codecs.StreamReader):
def StrictReplace(stream, errors='strict'):
    return utf_8.StreamReader(stream, errors)

# Python 2.x only
#class StreamWriter(utf_8
