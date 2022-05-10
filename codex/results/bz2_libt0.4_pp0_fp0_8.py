import bz2
bz2.decompress(compressed_data)

# bz2.compress()
# bz2.decompress()

# bz2.BZ2Compressor()
# bz2.BZ2Decompressor()

compressor = bz2.BZ2Compressor()
compressor.compress(data)
compressor.compress(more_data)
compressor.flush()

decompressor = bz2.BZ2Decompressor()
decompressor.decompress(compressed_data)
decompressor.decompress(more_compressed_data)

# zlib
import zlib
zlib.compress(data)
zlib.decompress(compressed_data)

# zlib.compress()
# zlib.decompress()

# zlib.compressobj()
# zlib.decompressobj()

compressor = zlib.compressobj()
compressor.compress(data)
compressor.compress(more_data)
compressor.flush()

decomp
