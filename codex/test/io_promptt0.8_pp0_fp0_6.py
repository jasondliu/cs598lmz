import io
# Test io.RawIOBase
# (an abstract class)
# Equivalent to io.FileIO
# io.RawIOBase has been renamed io.RawIOBase.
# io.RawIOBase is the abstract base class for raw binary I/O.
# This class supports the interface needed by io.FileIO.
# Read-only attributes:
#   mode : str. The I/O mode for the raw stream.
#   name : str. The name of the raw stream.
#     The name is the same as the file name given in the constructor.
#     This is not necessarily the file name used on the filesystem.
# The following methods must be implemented in derived classes:
#     readinto()
#     write()
#
# Note that read() and readall() are defined as methods to use with
# the buffer interface. Raw streams are not seekable.

# The following methods may be implemented in derived classes,
# but are not required.
#     close()
#     flush()
#     fileno()
#     isatty()
#     readable()
#     seekable()
#     writable()
#
# Note
