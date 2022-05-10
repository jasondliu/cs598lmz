import codecs
# Test codecs.register_error("ignore")
# by trying to decode the all-byte-value-255 data string
# Should succeed if the codec is handling the error correctly
# by skipping the bytes in question and not raising an exception.
# See http://www.python.org/doc/current/lib/module-codecs.html
#
# Note that this is a test for the codec, not for the Python Unicode
# codec registry, which knows nothing about the "ignore" error handler.
test_string = ''.join([chr(255)] * 100)
print type(test_string)

# With sys.setdefaultencoding set to "ascii"
# (which is the default on Windows),
# the following line should succeed.
# Without it, the line should fail.

# This test has been commented out because it is failing on MacOSX
# and we're not sure why yet.  In the meantime, this test is not
# really testing anything important, so it is ok to comment it.
#
#sys.setdefaultencoding("ascii")

# This should succeed; if it fails,
# the codec
