import bz2
# Test BZ2Decompressor function
from bz2 import BZ2Decompressor

# Uncompress data
dec = BZ2Decompressor()
uncompressed = dec.decompress(compressed)

# Compress data
compressed = BZ2Compressor().compress(uncompressed)

# Compress data
compressed = bz2.compress(uncompressed)

# Uncompress data
uncompressed = bz2.decompress(compressed)

# Compress data
compressed = bz2.compress(uncompressed)

# Uncompress data
uncompressed = bz2.decompress(compressed)
# Open bz2 file with context manager
import bz2

with bz2.open('output.txt.bz2', 'wt') as output_file:
    output_file.write('Contents of the example file go here.\n')
    output_file.write('And here, and here, and here,\n')
    output_file.write('and here, and here, and here.')

# Open
