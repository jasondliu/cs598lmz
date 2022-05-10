import bz2
bz2.decompress(compressed)

# bz2.compress() also accepts an optional argument for the compression level,
# which can be an integer between 1 and 9.

# The higher the compression level, the more time bz2.compress() will take
# to do its work.
# The tradeoff is that higher compression levels use less space to store the
# compressed data.

# The default compression level is 9.

# The bz2 module also contains a convenience function, bz2.open(),
# that works like the built-in function open(),
# but opens bzip2-compressed files in a way that lets you read and write them
# as plaintext files.

# The following example shows how to create a bzip2-compressed file
# and write some text to it:

import bz2
uncompressed_data = b"Lots of content here"
compressor = bz2.BZ2Compressor()
compressed_data = compressor.compress(uncompressed_data)
compressed_data += compressor.flush()

# The bz2.
