import codecs
# Test codecs.register_error, and make sure that the default error
# handler is used if the error handler is not found.

# This test is skipped on platforms that don't have the iconv_codec
# module, because it uses the "undefined" error handler, which is
# only available in iconv_codec.

import sys
import os

