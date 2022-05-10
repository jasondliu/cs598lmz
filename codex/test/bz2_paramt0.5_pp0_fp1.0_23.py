from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(b'\x42\x5a\x68\x39\x31\x41\x59\x26\x53\x59')

# bz2.BZ2Decompressor.decompress(data)
# Decompress data, returning uncompressed data as bytes.

# If you use an empty bytes object as the data, the decompressor will return
# any unconsumed input as a bytes object.

# If you use an empty bytearray object as the data, the decompressor will
# return any unconsumed input as a bytearray object.

# If you use a non-empty bytes or bytearray object, any unconsumed input
# will be added to the end of the object you passed in.

# If the decompressor runs out of input, it will raise EOFError.

# If the decompressor detects any errors, it will raise a ValueError.
