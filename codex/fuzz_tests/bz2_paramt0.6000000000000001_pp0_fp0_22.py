from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(compressed_data)

# Compress data iteratively
import bz2
uncompressed_data = b'\n'.join(lines)
compressor = bz2.BZ2Compressor()
compressor.compress(uncompressed_data)
compressor.flush()
compressed_data = compressor.compress(uncompressed_data)

# Compress data using context manager
import bz2
uncompressed_data = b'\n'.join(lines)
with bz2.BZ2File('compressed.bz2', 'wb') as f:
    f.write(uncompressed_data)

# Decompress data using context manager
with bz2.BZ2File('compressed.bz2', 'rb') as f:
    data = f.read()

# Compress data using context manager
import bz2
uncompressed_data = b'\n'.join(lines)
with bz2.open('compressed.bz2', 'wt') as f:
    f.write(uncomp
