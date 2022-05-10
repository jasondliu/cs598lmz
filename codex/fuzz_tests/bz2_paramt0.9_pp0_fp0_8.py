from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2_data)

# Difficult: Write a method for decompressing that can decompress any chunked-encoding, 
# not just bz2. Basically, a trickier part of the decompress function.
