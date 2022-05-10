import bz2
# Test BZ2Decompressor
from bz2 import BZ2Decompressor
decompressor = BZ2Decompressor()
decompressor.decompress(compressed_content)

# Test bz2.open()
with bz2.open(filename, mode='wt') as file:
    file.write(content)
with bz2.open(filename, mode='rt') as file:
    print(file.read(10))

# Test bz2.compress()
compressed_content = bz2.compress(content)

# Test bz2.decompress()
decompressed_content = bz2.decompress(compressed_content)

# Test bz2.BZ2Compressor
compressor = bz2.BZ2Compressor()
compressor.compress(content)
compressor.flush()

# Test bz2.BZ2Decompressor
decompressor = bz2.BZ2Decompressor()
decompressor.decompress(compressed_content)

# Test bz2.compress()

