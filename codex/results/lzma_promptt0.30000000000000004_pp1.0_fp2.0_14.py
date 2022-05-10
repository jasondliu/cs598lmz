import lzma
# Test LZMADecompressor

# LZMADecompressor.decompress(data, max_length=None)
# Decompress data, returning uncompressed data as bytes.
# If the data is incomplete or corrupt, the value of max_length determines what data will be returned as follows:
#
# * None (the default value of max_length): if any data is corrupted, raise an EOFError.
# * 0: always return as much data as possible. In this case, the return value may be more than the length of the input data if the input data was truncated or if the data stream was corrupted.
# * > 0: return at most max_length bytes of data. In this case, if any data is corrupted and the total amount of data returned reaches max_length, raise an EOFError.
#
# If the data stream is not corrupted, the return value may be less than max_length, but it will never be more.
#
# When using decompress() to decompress data incrementally, be aware that the decompressor object may still contain internal state from the previous call to decompress().
# The new data to be decompressed should be supplied in
