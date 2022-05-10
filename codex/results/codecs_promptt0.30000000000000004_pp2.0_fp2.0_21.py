import codecs
# Test codecs.register_error

# This test is not exhaustive.  It only tests the error handlers
# that are actually used by the codecs module.

# Error handler tests

# The following error handler tests are based on the error handler
# tests in the Python test suite.

def test_strict(errors):
    # Test the strict error handler
    for msg, s in (("illegal multibyte sequence", b"\xff"),
                   ("illegal multibyte sequence", b"\xc0\x80"),
                   ("illegal multibyte sequence", b"\xc0\xaf"),
                   ("illegal multibyte sequence", b"\xc1\x80"),
                   ("illegal multibyte sequence", b"\xc1\xbf"),
                   ("illegal multibyte sequence", b"\xc2\x80"),
                   ("illegal multibyte sequence", b"\xc2\xbf"),
                   ("illegal multibyte sequence", b"\xc3\x80"),
                   ("illegal multibyte sequence", b"\xc3\xbf"),
                   ("illegal multiby
