import bz2
bz2.decompress(bz2.compress(b'Hello World!'))

# bz2.compress() returns a bytes object, and bz2.decompress() requires a bytes-like object.
# The easiest way to get these is with the bytes() and bytearray() types introduced in Python 3.

# The compress() and decompress() functions each take a single parameter, which can be any type of object
# (such as a string) that supports the buffer protocol.
# The compress() function returns a bytes object, and decompress() requires a bytes-like object.

# The compress() function takes an optional second argument that controls the compression level.
# The value can range between 1 and 9, and the default is 9.
# The higher the value, the more aggressive the compression, but the longer it takes to complete.

# The compress() and decompress() functions are not thread safe.
# If you need to use them in parallel, you must use the BZ2Compressor and BZ2Decompressor classes instead.

# The BZ2Compressor and BZ2Decompressor classes are designed
