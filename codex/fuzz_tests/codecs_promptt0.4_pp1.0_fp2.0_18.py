import codecs
# Test codecs.register_error, and make sure that the default error
# handler is used if the error handler is not found.

# This test is skipped on platforms that don't have the iconv_codec
# module, because it uses the "undefined" error handler, which is
# only available in iconv_codec.

import sys
import os

from test import test_support

if test_support.is_jython:
    raise test_support.TestSkipped("Jython doesn't have the iconv_codec module")

# Skip test if the iconv_codec module is not available
try:
    import iconv_codec
except ImportError:
    raise test_support.TestSkipped("iconv_codec module not available")

# Try to use the "undefined" error handler
try:
    codecs.lookup_error("undefined")
except LookupError:
    raise test_support.TestSkipped("iconv_codec module doesn't have the 'undefined' error handler")

# Define a custom error handler
def custom_error_handler(error):
   
