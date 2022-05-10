import lzma
# Test LZMADecompressor
#
# If you have a file compressed with the LZMA algorithm (such as one ending
# in .xz) you can read it as follows:
#
# with lzma.open(filename, "rb") as f:
#    file_content = f.read()
#
# There is no need to decode the file content from bytes, as both the LZMA
# file format and this module's API always use bytes.
#
# The lzma module also provides an LZMAFile class which is a file-like object
# for reading and writing LZMA-compressed files.
#
# The LZMAFile class works in a similar way to the BZ2File class and the
# gzip.GzipFile class.
#
# LZMAFile objects have a peek() method which allows you to look at the next
# byte in the file without advancing the file position.
#
# LZMAFile objects also have a write() method which allows you to write
# compressed data.
#
# You can create an LZMAFile object in a with statement, which will automatically
# close the
