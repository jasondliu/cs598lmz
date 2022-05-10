import codecs
# Test codecs.register_error
#
# The codecs module is not part of the standard library in Python 2.2,
# so we have to check for its presence.

try:
    import codecs
except ImportError:
    raise ImportError("this test needs the 'codecs' module")

import unittest
