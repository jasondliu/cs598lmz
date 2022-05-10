import io
# Test io.RawIOBase; this gives us a good test of io.IOBase and its
# error handling as well.
#
# RawIOBase has been designed as a very simple replacement for the
# old raw file interface.
#
# The class has no read() or write() methods by itself. The main
# reason for this is that there are too many possible signatures for
# write(). It is an error for a subclass to define read() or write()
# unless it is able to handle all possible signatures.
#
# An inheriting class may define readinto() for more efficient reading
# of data into buffers. It may choose to define readinto1() for even
# more efficient reading (readinto1() must return at most one byte
# less than the length of the buffer, however).
#
# If the subclass has a concept of "end of stream", it should define
# readable() to return False when the stream is closed or if it has
# reached a point where reading returns an empty string. It should
# be noted that some RawIOBase subclasses (such as BufferedReader)
# are always readable.

class TestRawIOBase:

    def
