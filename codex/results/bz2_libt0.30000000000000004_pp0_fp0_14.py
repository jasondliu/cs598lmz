import bz2
bz2.decompress(bz2_data)

# bz2.BZ2File
# bz2.BZ2File(filename, mode='r', buffering=None, compresslevel=9)
# BZ2File is a subclass of io.BufferedIOBase, and provides a buffered interface to binary files containing bzip2-compressed data.
# The mode parameter can be either 'r' or 'w', for reading (default) or writing.
# The compresslevel parameter is an integer from 1 to 9 controlling the level of compression; 1 is fastest and produces the least compression, 9 is slowest and produces the most.
# The default is 9.

# The BZ2File class provides the following methods:

# BZ2File.read([size])
# Read up to size uncompressed bytes from the file. If the size argument is negative or omitted, read until EOF is reached.
# Returns a bytes object.

# BZ2File.readline([size])
# Read a line from the file. The terminating newline (if present) is retained. If the size argument is present and non-
