import lzma
# Test LZMADecompressor

# Test that the LZMADecompressor class can be used to decompress data
# produced by the LZMA library.

# The data used for testing was produced by the LZMA command line tool
# using the command:
#     lzma -z -k file.txt
# where file.txt is a text file containing the text "Hello World!\n".

# The data was then hexlified and pasted into the DATA string below.

