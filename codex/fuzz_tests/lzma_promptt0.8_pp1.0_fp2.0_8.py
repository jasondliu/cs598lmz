import lzma
# Test LZMADecompressor by decompressing data with known result.

compressed = lzma.compress(b'The quick brown fox jumped over the lazy dog.')
decomp = lzma.LZMADecompressor()
result = decomp.decompress(compressed)
assert result == b'The quick brown fox jumped over the lazy dog.'
"""

"""
# Read all data from a file (or stream), and decompress it in one step.
# This is simpler than the decompress() example above, and is the
# preferred way if all of the data for decompression is available and
# fits comfortably into memory.

with open('example.xz', 'rb') as f:
    file_content = f.read()

decompressed_data = lzma.decompress(file_content)
"""

"""
with lzma.open(self.dbName, mode='rt') as f:
    for line in f:
        print(line)
"""

"""
with open('example.xz', 'rb') as f:
    data = f.read()

# Re
