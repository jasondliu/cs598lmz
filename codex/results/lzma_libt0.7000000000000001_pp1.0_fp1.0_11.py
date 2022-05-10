import lzma
lzma.LZMACompressor.__doc__ = """\
Compress data incrementally.

All data input must be passed through one or more calls to the
compress() method. After all data has been processed, call the flush()
method to finish the stream.

Only call the compress() method when the filter_size parameter is
None.

The compress() method returns a bytes object containing the compressed
data if filter_size is zero and the flush() method returns the data
left in internal buffers as a bytes object.

If the filter_size is not zero, the compress() method returns the
filter ID (an integer) followed by the compressed data. The flush()
method returns the filter ID, followed by the data left in internal
buffers and the filter properties as a bytes object.
"""

# pylint: disable=no-member

class LZMACompressor(lzma.LZMACompressor, object):

    def __init__(self, format=lzma.FORMAT_ALONE, check=-1, preset=None, filters=None):
        super(LZMACompressor, self
