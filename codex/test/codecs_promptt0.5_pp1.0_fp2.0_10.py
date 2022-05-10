import codecs
# Test codecs.register_error()
# See also test_codecs.py
#
# This test needs to be executed in a separate process because
# it needs to register a new codec error handler.
#
# Test for issue #1558: codecs.register_error() doesn't work
# with 'replace' and 'xmlcharrefreplace'

import sys
import unittest
