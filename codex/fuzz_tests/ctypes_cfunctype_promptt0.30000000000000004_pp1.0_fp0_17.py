import ctypes
# Test ctypes.CFUNCTYPE()

# This test is a bit different from the others.  It just checks
# that ctypes.CFUNCTYPE() doesn't crash.

# This test is also a bit different from the others in that it
# doesn't use the test_support module.  That's because this test
# is designed to be run in the background, and it's not really
# appropriate to have a test that's constantly running in the
# background.  (It's not a problem for the other tests because
# they're so fast that they don't really have much impact on
# performance.)

# This test is also a bit different from the others in that it
# doesn't use the unittest module.  That's because this test
# is designed to be run in the background, and it's not really
# appropriate to have a test that's constantly running in the
# background.  (It's not a problem for the other tests because
# they're so fast that they don't really have much impact on
# performance.)

# This test is also a bit different from the others in that it
# doesn't use the logging module.  That
