import io
# Test io.RawIOBase
#
# This test checks that io.RawIOBase works as expected.
# It does so by creating a raw IO implementation (BytesIOModule)
# and checking that it passes the io.RawIOBase test suite.
#
# io.RawIOBase is an abstract class, so it cannot be instantiated.
# Instead, an instance of BytesIOModule is created and passed to
# io.RawIOBase's constructor.
#
# The test suite is run by calling the run method.
#
# Note: The test suite assumes that the underlying raw IO
# implementation works as expected.
#
# Implementation notes:
#
# The test suite uses a lot of magic numbers.
# They are usually explained in comments.
#
# The test suite also assumes that the underlying raw IO
# implementation is able to seek to any position in the stream.
#
# The test suite assumes that the underlying raw IO
# implementation is able to read at most 65536 bytes at a time.
#
# The test suite assumes that the underlying raw IO
# implementation is able to write at most 65536 bytes at a time.
#
