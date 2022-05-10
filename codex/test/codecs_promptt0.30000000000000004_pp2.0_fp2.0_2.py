import codecs
# Test codecs.register_error

# This test is not exhaustive, but it should catch most of the
# problems.

# The tests are run twice: once with the default 'strict' error
# handler, and once with a custom 'ignore' error handler.

# The custom error handler is necessary to test the error handler
# registration mechanism.

import codecs
import unittest

