from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(b'\x42\x5a\x68\x39\x31\x41\x59\x26\x53\x59')

# bz2.BZ2Decompressor.decompress(data)
# decompress(data, max_length=-1)
# Decompress data, returning uncompressed data as bytes.
# If the data is incomplete or corrupt, the behaviour of this method is undefined.

# If the data is valid and stream is False, returns the uncompressed data as bytes.
# If stream is True, returns a generator object that yields uncompressed data as it becomes available.
# If max_length is non-negative, the generator is limited to returning at most max_length bytes of uncompressed data.
# In this case the generator will raise an exception when an attempt is made to decompress more than max_length bytes.

# If max_length is negative, the generator can return between 0 and infinity bytes of uncompressed data.
# If the data is valid and stream is False, returns the uncompressed data as bytes.
# If stream is True, returns a generator object that
