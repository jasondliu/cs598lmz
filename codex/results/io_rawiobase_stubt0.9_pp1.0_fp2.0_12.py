import io
class File(io.RawIOBase):
    """An interface to raw streams of data.

    It defers some Python functions so that the values returned by
    those functions continue to reflect the current state of the
    stream.

    File objects should be closed explicitly, with close().
    """

    # The maximum number of unused bytes to hold in memory for the next
    # read() or write() operation.
    #
    # Note: The max_buffer_size is a relatively small amount that allows
    # raw streams to read or write a reasonable amount of data without
    # having to wait.
    #
    # Most of the time, the raw stream implementation will want to
    # use the wait_until_readable() and wait_until_writable() functions
    # to wait until the underlying transport has some space to write
    # or some data to read.
    #
    # This can be overridden by a subclass or by any context or
    # event loop by setting max_buffer_size in their __init__() methods.

    max_buffer_size = 2048

    def readable(self):
        return True

    def writable(self):
        return
