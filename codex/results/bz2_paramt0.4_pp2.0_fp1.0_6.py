from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2.compress(data))

# The bz2 module also provides a way to create BZ2Compressor and BZ2Decompressor objects that can be used to incrementally compress or decompress data streams.

# The compress() method works like compress_into() but returns the compressed data as a bytes object rather than writing it into a file.

# The decompress() method works like decompress_from() but reads compressed data from a bytes object rather than a file.

# The compress() and decompress() methods are also available as instance methods of BZ2Compressor and BZ2Decompressor objects.

# The BZ2Compressor class also provides a flush() method, which returns the compressed data generated so far and resets the compressor object to its initial state.

# The BZ2Decompressor class also provides an unused_data attribute, which contains the unused portion of the input data passed to the decompress() method.

# The compress() and decompress() methods of BZ2Compressor and BZ2Decompressor objects can be called multiple times to incrementally compress or decompress a data
