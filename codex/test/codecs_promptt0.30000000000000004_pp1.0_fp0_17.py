import codecs
# Test codecs.register_error

# This test is not exhaustive.  It only tests the error handling
# mechanism, not the codecs themselves.

# The tests are designed to be run with the locale C so that we can
# test the fallback to the 'replace' handler.

import codecs, encodings.iso8859_1, encodings.iso8859_2
