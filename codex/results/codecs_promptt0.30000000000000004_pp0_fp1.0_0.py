import codecs
# Test codecs.register_error

def test_register_error():
    # Test codecs.register_error
    #
    # This is a bit tricky, because the codecs module doesn't have a
    # public API to retrieve the currently registered errors.
    #
    # The test consists of two parts:
    # 1. Register a new error handler, check that it works
    # 2. Restore the original error handler, check that it works
    #
    # The first part is implemented by encoding a string with a
    # character that is not in the target encoding.  The second part
    # is implemented by encoding a string with a character that is not
    # in the target encoding, but that is replaced by a question mark
    # by the original error handler.
    #
    # Note that the test is not completely correct, because it is
    # possible that the original error handler is one that replaces
    # unknown characters with question marks.  However, this is very
    # unlikely.
    #
    # Note that this test is not run when the test is run with -ugui,
    # because the test output is not easily visible in the
