import bz2
# Test BZ2Decompressor

# The first step is to create a BZ2Decompressor object. This object will keep
# track of the state of decompression so that you can decompress a file in a
# single call or in multiple calls.

# The data parameter to the BZ2Decompressor.decompress() method is the data to
# decompress. The max_length parameter is the maximum amount of data to return.
# If the data parameter contains more data than max_length, the data will be
# decompressed and the excess data will be buffered for the next call to the
# decompress() method.

# The return value is the decompressed data, which may be smaller than the
# amount of data passed in. If the decompressed data is larger than the
# max_length parameter, only max_length bytes will be returned, but more data
# will be buffered for the next call to decompress().

# If the input data is invalid, a ValueError is raised.

# If the data parameter is empty, the return value is an empty bytes object.
# If the data parameter is omitted, the return value is the remaining buffered
