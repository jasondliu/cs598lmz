from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(b'\x42\x5a\x68\x39\x31\x41\x59\x26\x53\x59\x99\x5e\x0c\x0a')

# bz2.BZ2Decompressor.decompress(data, size=0):
# Decompress *data*, returning uncompressed data as bytes.
# If *size* is non-zero then decompress *data* into *size* bytes of uncompressed data.
# If *size* is zero, or not specified, then decompress until the end of the data is reached.

# If the compressed data stream is corrupted, this method may raise a ValueError.
# If *size* is non-zero and the amount of uncompressed data specified by *size* cannot be produced, a ValueError is raised.

# If any data is decompressed, the decompressor object will be in the eof state.
# If no data is decompressed, the decompressor object will have the unused_data attribute set to the data parameter.
