import codecs
# Test codecs.register_error()
#
# The following codecs are registered:
#
# - 'surrogateescape' which replaces malformed data by the unicode
#   character U+DCxx.
#
# - 'backslashreplace' which replaces malformed data by a \xNN
#   escape.
#
# - 'strict' which raises a UnicodeDecodeError.
#
# - 'surrogatepass' which leaves malformed data unchanged (XXX this
#   is not supported yet)
#
# - 'ignore' which ignores malformed data (XXX this is not supported
#   yet)
#
# - 'replace' which replaces malformed data by a '?' (XXX this is not
#   supported yet)
#

import sys
import unittest

from test import test_support

#
# This is a list of test cases. Each test case is a tuple
#
#     (input, errors, output, error_flag)
#
# - input is a unicode string
#
# - errors is the error handling name
#
# - output is the expected result (a unicode string
