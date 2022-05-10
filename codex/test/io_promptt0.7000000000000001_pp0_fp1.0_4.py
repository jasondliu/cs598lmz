import io
# Test io.RawIOBase
# File-like objects that read from or write to a raw device.
# Unlike regular files, their raw attribute is always true.
# They have no name attribute and no fileno() method.
# They do have a mode attribute and a readable() or writable() method.

class RawI(io.RawIOBase):
    def read(self, n=-1):
        # Return up to n bytes.
        # Only makes sense for reading.
        pass

    def write(self, b):
        # Write the given bytes.
        # Only makes sense for writing.
        pass


# Test io.BufferedIOBase
# File-like objects that buffer I/O.
# They have a peek() method and a readable() or writable() method.

class BufferedI(io.BufferedIOBase):
    def read(self, n=-1):
        # Return up to n bytes with at least one byte read, unless EOF is hit.
        # Only makes sense for buffered reading.
        pass

