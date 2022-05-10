import codecs
# Test codecs.register_error(encoding, handler)

# This test comes from the bug report:

# http://python.org/sf/735208
#     'iso-8859-1' codec can't decode byte 0x91 in position 0: ordinal not in range(256)

# The codec should not be able to decode the byte 0x91 (decimal 145, left
# single quote), but it should not raise an exception either.

def codec_not_found(exc):
    print("Codec not found: ", exc)

# Register an error handler to ignore the error.
codecs.register_error("ignore", codec_not_found)

# This string contains an invalid byte 0x91
# a test
s = '\x91 a test \x91'

# When we call .decode() it should not raise an exception.
print(s.encode("iso-8859-1").decode("iso-8859-1", "ignore"))

# This is what it should print:
#   n a test n

### XXX: remove this and add a test for the built
