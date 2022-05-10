from lzma import LZMADecompressor
LZMADecompressor().decompress(b'\x10\xd5\xc0\xcc\x0b\xa1\x01\x10\x00\x00\x00\x00\x00').decode()

# Output:
# 'hello world\n'

# Once the LZMA object has been fed enough data and produced enough output to
# satisfy the input and output size limits, it will raise an EOFError exception
# (the same exception raised when the end of a file is reached).  If the parameters
# used to create the LZMA object do not allow the entire compressed stream to
# be processed, then the object can be used as a context manager in a with statement.
# This will cause the LZMADecompressor.flush() method to be called automatically,
# which will allow any data processed so far to be returned and any remaining data
# to be discarded or saved for later processing.
