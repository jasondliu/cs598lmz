import io
# Test io.RawIOBase

# This is a test for the io.RawIOBase class, which is the base implementation
# of the raw I/O interface.  This class is not intended to be instantiated
# directly, but rather to be extended.  The constructor should be called via
# the super class, i.e. super(RawIOBaseSubClass, self).__init__(name)

# This test suite should be run with a variety of RawIOBase subclasses,
# including a simple subclass that just defines read and write, and a
# subclass which implements readinto and write.  In both cases, the
# subclass should be tested with and without a working seek method.

# The test suite should also be run with a variety of different
# implementations of the underlying buffer object, including StringIO,
# BytesIO, and a custom class that implements the buffer protocol.

# The test suite should also be run with and without threading, to ensure
# that there are no thread-safety issues.


# The test suite assumes that the subclass of RawIOBase has been
# instantiated with a buffer object, and that the buffer object has the
#
