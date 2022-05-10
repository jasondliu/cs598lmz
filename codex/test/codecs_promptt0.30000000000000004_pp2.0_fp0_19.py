import codecs
# Test codecs.register_error
#
# This test is a little tricky.  We have to make sure that the
# codecs module is loaded before we register the error handler.
# Otherwise, the error handler won't be found.  We also can't
# use the codecs module in this test, since that would cause
# the codecs module to be loaded.
#
# The test is run twice.  The first time, we register the error
# handler, and the second time, we don't.  In both cases, we
# try to decode a string with a character that can't be decoded.
# If the error handler is registered, the string should be decoded
# successfully.  If the error handler isn't registered, the string
# should fail to decode.

# Make sure the codecs module isn't loaded yet.
try:
    codecs
except NameError:
    pass
else:
    print("codecs module already loaded")
