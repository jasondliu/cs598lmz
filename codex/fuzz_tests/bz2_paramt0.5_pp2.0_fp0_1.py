from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084')

# The bz2 module includes a complete implementation of bzip2 compression.
# The compress() and decompress() functions both take a byte string.
# The decompress() function also has an optional max_length parameter.
# If you try to decompress more than max_length bytes, ValueError will be raised.
# The decompress() function will raise an EOFError if the compressed data doesn't end
# when it should, or if there is more than one concatenated stream.
# The decompressor object can be used to decompress a series of compressed streams.
# The decompress() method will return empty bytes objects until the end of the compressed stream is reached.
# The decompressor object can be used as a context manager.
# In this case, the
