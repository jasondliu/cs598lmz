import bz2
bz2.decompress(bz2.compress(bytes("hello world", "utf-8")))

# The bz2 module provides a comprehensive interface for the bz2 compression library. 
# It implements a complete file interface, one shot (de)compression functions, and types for sequential (de)compression.

# Compress data in one shot
import bz2
data = b"Lots and lots of data."
compressed = bz2.compress(data)
print(compressed)

# Decompress data in one shot
import bz2
data = b"Lots and lots of data."
compressed = bz2.compress(data)
print(compressed)
decompressed = bz2.decompress(compressed)
print(decompressed)

# Compress data incrementally
import bz2
data = b"Lots and lots of data."
compressor = bz2.BZ2Compressor()
compressed = compressor.compress(data)
print(compressed)
compressed += compressor.flush()
print(compressed)


