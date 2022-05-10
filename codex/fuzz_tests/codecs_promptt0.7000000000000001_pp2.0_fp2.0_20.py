import codecs
# Test codecs.register_error
# (See http://bugs.python.org/issue6202)
codecs.register_error('strict', codecs.strict_errors)
codecs.register_error('ignore', codecs.ignore_errors)
codecs.register_error('replace', codecs.replace_errors)

import sys
import io
import os
import unittest
import warnings
import traceback

if sys.platform != "win32":
    CODEC_SEARCH_PATH = [os.path.join(sys.base_prefix, 'lib', 'python' + sys.version[:3], 'test', 'test_support')]
else:
    CODEC_SEARCH_PATH = []

# Exception raised in case an encoding can't be found
class CodecRegistryError(LookupError, SystemError):
    pass

# The search functions for the encodings package.
#
# Each of these is called as a function with one argument, the
# encoding name in all lower case letters.  The function is
# expected to return a tuple of functions (encoder, dec
