import codecs
# Test codecs.register_error
#
# This test is expected to FAIL
#
# The codecs.register_error() function should register an alternate
# error handler for a given encoding.
#
# This test makes sure that the module is present and that it fails
# as documented.

import codecs
try:
    codecs.register_error()
except TypeError:
    print("OK")
else:
    print("ERROR")
