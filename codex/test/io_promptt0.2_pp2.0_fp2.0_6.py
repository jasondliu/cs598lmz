import io
# Test io.RawIOBase
#
# Test that io.RawIOBase is a base class for raw binary I/O.
#
# The io module defines a set of base classes for standard I/O:
# TextIOBase, RawIOBase, BufferedIOBase, and their subclasses.
#
# The RawIOBase class defines a raw binary I/O interface,
# and its subclasses define concrete implementations of that interface.
#
# The RawIOBase class is not meant to be instantiated directly,
# but rather to be subclassed by concrete implementations.
#
# The RawIOBase class defines the following methods:
#
# readinto(b)
#     Read up to len(b) bytes into the writable buffer b,
#     and return the number of bytes read.
#     If the object is in non-blocking mode and no bytes are available,
#     None is returned.
#     If the object is in blocking mode and no bytes are available,
#     the method blocks until at least one byte is available or
#     until the end of the stream is reached.
#     When no more data is available,
#     and
