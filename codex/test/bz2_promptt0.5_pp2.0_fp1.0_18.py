import bz2
# Test BZ2Decompressor
#
# The BZ2Decompressor class supports incremental decompression.
#
# The decompress() method can be called multiple times with new data
# and returns the decompressed data left over from the last call.
#
# The unused_data attribute can be queried to find the data that could
# not be decompressed (used for seeking backwards).

data = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
compressor = bz2.BZ2Compressor()
decompressor = bz2.BZ2Decompressor()

# Compress some data
compressed = compressor.compress(data)
# Flush the compressor, so we can decompress it incrementally
compressed += compressor.flush()

# Decompress some data
