from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2_data)

# The same as above but with context manager
with BZ2Decompressor() as dec:
    data = dec.decompress(bz2_data)

# Decompressing multiple compressed streams
with BZ2Decompressor() as dec:
    for chunk in chunks:
        data = dec.decompress(chunk)

# Compressing data
import bz2
bz2.compress(data)

# Compressing data with context manager
with bz2.BZ2Compressor() as comp:
    for chunk in chunks:
        comp.compress(chunk)
    compressed = comp.flush()

# Compressing data in memory
bz2.compress(data)

# Compressing data in memory with context manager
with bz2.BZ2Compressor() as comp:
    comp.compress(data)
    compressed = comp.flush()

# Compressing data in memory with context manager
with bz2.BZ2Compressor() as comp:
    comp.compress(data
