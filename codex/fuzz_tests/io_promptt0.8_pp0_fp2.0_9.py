import io
# Test io.RawIOBase.readall documentation.

import io

# io.RawIOBase.readall should return a bytes object.  The bytes object
# returned must be non-empty if the io.RawIOBase object is not in
# non-blocking mode and has at least one byte available.
#
# io.RawIOBase.readall should raise io.BlockingIOError on a non-blocking
# raw I/O object in the case of no available data.
def test_rawiobase_readall():
    # The behavior of io.RawIOBase.readall exists in the C implementation
    # of _pyio.  If the readinto() method exists, then the readall() method
    # is implemented.  This is the case with _io.FileIO and _io.BytesIO.
    # The _io.BufferedReader class, on the other hand, does not provide
    # readinto() and therefore _io.BufferedReader.readall() raises
    # io.UnsupportedOperation.  This test is not concerned with that case.
    #
    # The implementation of io.RawIOBase.read
