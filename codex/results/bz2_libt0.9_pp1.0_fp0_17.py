import bz2
bz2_object = bz2.BZ2File('example.bz2')
data = bz2_object.read()
bz2_object.close()
len(data)

# 'example.txt' and 'example_compressed.bz2' refer to the same data.

# In general, using the optimized formats will result in much smaller files.
# In many cases, the compressed data can be read and processed in lazily, one
# piece at a time, which is often ideal for processing larger files.

# Compressed files
# Compressed files act like both a file object and a context manager
# 'filenmame' must be str or bytes, not Path!

# bz2.BZ2File(filename, mode='r', buffering=0, compresslevel=9):
# mode options: 'r', 'rb', 'w', 'wb', 'x', 'xb', 'a', or 'ab'
# buffering options: 1, 2, 0 (default) or -1 (buffer system default).
# compresslevel: 0-9.

# gzip.Gzip
