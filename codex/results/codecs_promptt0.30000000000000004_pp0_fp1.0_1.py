import codecs
# Test codecs.register_error
#
# This test is a bit tricky.  We have to make sure that the
# codecs.register_error function is called before the codecs module
# is loaded.  We do this by importing the test_register_error module
# before the codecs module is loaded.

# This test is also tricky because it is not possible to unregister
# an error handler.  So we have to make sure that the codecs module
# is reloaded between each test.

# The test_register_error module contains a function that registers
# an error handler for the 'test' codec.  The error handler is
# defined in this module.

# The test_register_error module also contains a function that
# registers a second error handler for the 'test' codec.  This
# error handler is also defined in this module.

# The test_register_error module also contains a function that
# registers an error handler for the 'test2' codec.  This error
# handler is defined in the test_register_error module.

# The test_register_error module also contains a function that
# registers a second error handler
