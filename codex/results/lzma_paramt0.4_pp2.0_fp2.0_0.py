from lzma import LZMADecompressor
LZMADecompressor.decompress(data)

# lzma.LZMADecompressor.decompress(data, max_length=None, format=FORMAT_AUTO, filters=None)
# data: the data to decompress.
# max_length: the maximum length of the decompressed data.
# format: the container format.
# filters: a list of filters to apply in order.

# The decompressor object can be used as a context manager. In this case,
# the decompressor is closed after the with statement, even if an exception occurs.

# The decompressor object can also be used as an iterator.
# Each call to the iterator’s next() method returns a chunk of decompressed data.
# The size of each chunk depends on the implementation and the input data.
# When all of the input data has been decompressed, calling the iterator’s next() method
# will raise an EOFError.

# The decompressor object can also be used as a context manager.
# In this case, the decompressor is closed after the with statement, even if an exception occurs.

# The decompressor
