import lzma
# Test LZMADecompressor

# Test that the LZMADecompressor class can be used to decompress data
# produced by the LZMA library.

# The data used for testing was produced by the LZMA command line tool
# using the command:
#     lzma -z -k file.txt
# where file.txt is a text file containing the text "Hello World!\n".

# The data was then hexlified and pasted into the DATA string below.

DATA = b'\xfd7zXZ\x00\x00\x04\xe6\xd6\xb4F\x02\x00!\x01\x16\x00\x00\x00t/\xca\xcc\xcf\xcb,I\xcd\xcf\xcc\xe5\x02\x00 \x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\
