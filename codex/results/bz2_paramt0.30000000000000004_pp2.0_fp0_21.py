from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(data)

# bz2.decompress(data)

# The bz2 module provides a comprehensive interface for the bz2 compression library. It implements a complete file interface, one shot (de)compression functions, and types for sequential (de)compression.

# The BZ2File class provides a file-like interface to a bzip2-compressed file, in that the open() function returns a file-like object which can be used in a with statement, or just called to return a decompressed file object.

# The compress() and decompress() functions provide one-shot (de)compression.

# The BZ2Compressor and BZ2Decompressor objects provide a streaming compression and decompression objects for sequential processing.

# The compress() and decompress() functions each take a single parameter, which can either be a byte string or a file object. If it is a byte string, the string is compressed and returned. If it is a file object, the contents of the file are compressed and saved to another file.

# The BZ2File class provides a file-like interface to a bzip2
