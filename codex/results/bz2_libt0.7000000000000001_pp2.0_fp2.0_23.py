import bz2
bz2.BZ2File.close(bz2_file)  # this is the same as bz2_file.close()

bz2_file = bz2.BZ2File('path/to/compressed/file/data.bz2', 'rb')
# The with statement calls bz2_file.close() automatically for you.
with bz2.BZ2File('path/to/compressed/file/data.bz2', 'rb') as bz2_file:
    data = bz2_file.read()
# The file is automatically closed when you exit the with statement.

# Compression level
bz2.BZ2File(
    'compressed_file.bz2',
    'wb',
    compresslevel=9,
)

# Writing compressed data
bz2_file = bz2.BZ2File(
    'example.bz2',
    'wb',
    compresslevel=9,
)
uncompressed_data = b'The same line, over and over.\n'
bz2
