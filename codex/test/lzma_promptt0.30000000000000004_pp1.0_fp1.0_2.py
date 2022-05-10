import lzma
# Test LZMADecompressor

# The LZMADecompressor class supports incremental decompression.
# The decompress() method can be called multiple times with new data and the
# uncompressed data will be returned.

# The decompressor object can be used as a context manager and in that case
# the decompress() method will not need to be called in order to finish the
# decompression process.

# The example below shows how to decompress data from a file.

import lzma

