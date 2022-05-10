from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(b'BZh91AY&SY\xc4\x98\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08')

# bz2.BZ2Decompressor.decompress(data, size=0)
# Decompress data, returning uncompressed data as bytes.
# If the data argument is omitted, read from the stream object file.
# If the data argument is present, the size argument is ignored and
# decompression is done straight from data.
# When using decompressor objects, it is recommended to feed data in
# chunks to the decompress() method in order to avoid excessive memory
# consumption via the internal buffer.
# The size argument is the initial size of the output buffer.
# The default is 0, meaning try to determine this automatically.
# If the decompressed data doesn’t fit into the output buffer,
# a larger buffer is allocated and the data is decompressed into the larger buffer.
# The buffer
