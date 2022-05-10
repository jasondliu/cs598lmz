import codecs
# Test codecs.register_error
#
# This test is a bit tricky, because we need to make sure that the
# codecs module is imported before we start registering errors.
#
# The easiest way to do this is to import the codecs module in this
# file, and then import this file from the test_codecs.py file.

