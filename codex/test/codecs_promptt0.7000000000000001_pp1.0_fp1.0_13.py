import codecs
# Test codecs.register_error()

# The tests in this file try to verify that the codecs.register_error
# function is present and works as advertised.

# The errorHandler should take two arguments: the UnicodeEncodeError and
# the encoder state.  The errorHandler should return a tuple (replacement,
# newPosition).  replacement is a unicode object that is inserted into
# the output stream, while newPosition tells the encoder object what it
# should do next.  newPosition should be one of the following three
# values:
#
#     -1 -- the encoder will raise the original exception again
#      0 -- the encoder will skip one input character and continue encoding
#      1 -- the encoder will continue encoding at the original position

import codecs
import string

# Simple error handler
