import bz2
# Test BZ2Decompressor and BZ2Compressor classes

# The BZ2Decompressor class is a stream decompressor that decompresses
# data read from a file-like object to another file-like object.
# The BZ2Compressor class is a stream compressor that compresses
# data read from a file-like object to another file-like object.

# The BZ2Decompressor and BZ2Compressor classes support the context
# management protocol.

# The BZ2Decompressor class supports the following methods:

# decompress(data)
#     Decompress data.

# flush()
#     Return any remaining decompressed data.

# The BZ2Compressor class supports the following methods:

# compress(data)
#     Compress data.

# flush(mode)
#     Return any remaining compressed data.

# The following example decompresses a file:

with open('example.bz2', 'rb') as input:
    decompressor = bz2.BZ2Decompressor()
