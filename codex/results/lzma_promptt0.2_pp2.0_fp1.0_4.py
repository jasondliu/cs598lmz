import lzma
# Test LZMADecompressor

# Test that the decompressor can decompress a file compressed with the
# command line tool xz.

# The test file is a concatenation of two files:
#
# - A file containing the text "Hello World!\n"
#
# - A file containing the text "Goodbye World!\n"

# The test file was compressed with the command line tool xz with the
# following command:
#
#     xz -z -k -e -9 -T0 testdata.txt

# The test file was created with the following commands:
#
#     echo "Hello World!" > testdata1.txt
#     echo "Goodbye World!" > testdata2.txt
#     cat testdata1.txt testdata2.txt > testdata.txt

# The test file is a concatenation of two compressed streams.

# The test file is compressed with the LZMA2 algorithm.

# The test file is compressed with the BCJ filter.

# The test file is compressed with the LZMA2 filter.

# The test file is compressed with the Delta filter.
