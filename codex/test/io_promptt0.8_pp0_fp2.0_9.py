import io
# Test io.RawIOBase.readall documentation.

import io

# io.RawIOBase.readall should return a bytes object.  The bytes object
# returned must be non-empty if the io.RawIOBase object is not in
# non-blocking mode and has at least one byte available.
#
# io.RawIOBase.readall should raise io.BlockingIOError on a non-blocking
# raw I/O object in the case of no available data.
