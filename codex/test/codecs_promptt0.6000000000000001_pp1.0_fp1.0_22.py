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

