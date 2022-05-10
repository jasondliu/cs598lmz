import codecs
# Test codecs.register_error
#
# This test is intended to be run with the -R option of regrtest.py.
#
# The test first registers an error handler, then checks that an encoding
# error is properly handled by our error handler.

# This error handler is registered by the test.
def handler(exception):
    return ('', len(exception.object))

# Register the error handler.
codecs.register_error('test.my_error_handler', handler)

# Check that the error handler works.
def test(encoding):
    # This will raise a UnicodeEncodeError.
    codecs.encode(u'\ud800', encoding, 'test.my_error_handler')

# Check that the error handler works for each of the built-in encodings.
# The encodings are chosen by looking at the aliases of the encodings
# listed in the Python source code (Modules/cjkencodings/_codecs.py).
for encoding in ('big5', 'big5hkscs', 'cp037', 'cp424', 'cp437', 'cp
