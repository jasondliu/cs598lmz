import codecs
# Test codecs.register_error()

# This test is a bit tricky because we have to generate an error
# message that is encoded in a codec that doesn't exist.  So we
# have to create a fake codec that raises an error on encode()
# and register it.

import codecs
