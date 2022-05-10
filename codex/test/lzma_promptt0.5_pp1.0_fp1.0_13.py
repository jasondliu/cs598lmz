import lzma
# Test LZMADecompressor.

# The source of the test data is the file "alice29.txt" from the
# Calgary Corpus.

# The LZMA SDK's "lzmadec" utility was used to compress the file
# and split it into two pieces.

# The test data contains the first (and only) LZMA stream in the file.

# The test data is encoded in hexadecimal.

# The uncompressed size is known.

# The first byte of the test data is the LZMA properties byte.

# The second byte through the tenth byte of the test data is the
# uncompressed size.  The uncompressed size is stored in little-endian
# order.

# The remaining bytes of the test data are the compressed data.

# The test data was generated with the following commands:

#   $ lzmadec alice29.txt -o alice29.lzma
#   $ ./hexify.py alice29.lzma.0
#   $ ./hexify.py alice29.lzma.1

# The first command creates the compressed file
