import bz2
# Test BZ2Decompressor
dec = bz2.BZ2Decompressor()
dec.decompress(file_content)

# Create a BZ2File Object
bz_file = bz2.BZ2File('data/compressed.bz2', 'w')
bz_file.write(file_content)
bz_file.close()

# Read from a BZ2 file
bz_file = bz2.BZ2File('data/compressed.bz2', 'r')
file_content = bz_file.read()
bz_file.close()

# Test BZ2Compressor
comp = bz2.BZ2Compressor()
comp.compress(file_content)

# Compress data with BZ2
compressed_content = bz2.compress(file_content)
decompressed_content = bz2.decompress(compressed_content)

# Test ZLIB
import zlib
file_content = b'This is the original text.'
compressed_content = zlib.compress(file_content
