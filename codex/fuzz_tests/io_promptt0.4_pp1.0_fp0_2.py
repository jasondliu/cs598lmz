import io
# Test io.RawIOBase
# this is the base class for raw binary I/O.
# It defines the basic interface to a stream.
# There is no readinto() because that's implemented in a derived class

# Test io.BufferedIOBase
# this is the base class for binary buffered I/O.
# It defines the basic interface, which requires
# a readinto() method.

# Test io.TextIOBase
# this is the base class for text I/O.
# It defines a read() method with an optional size argument,
# readline(), readlines(), and writelines().
# There is no readinto() because that's implemented in a derived class

# Test io.BytesIO
# this implements a file-like class,
# using an in-memory bytes buffer.
# It inherits io.RawIOBase

# Test io.StringIO
# this implements a file-like class,
# using an in-memory unicode buffer.
# It inherits io.TextIOBase

# Test io.FileIO
# this implements a file-like class,
# using a real file descriptor.
# It inher
