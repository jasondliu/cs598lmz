import lzma
# Test LZMADecompressor

# Get a compressed file
with open('../data/xz/enwik8', 'rb') as f:
    compressed = f.read()

# Decompress it
decompressor = lzma.LZMADecompressor()
decompressed = decompressor.decompress(compressed)

# Check that the decompressed file is the same as the original
with open('../data/enwik8', 'rb') as f:
    original = f.read()
assert decompressed == original
 
# Test LZMAFile

# Get a compressed file
with open('../data/xz/enwik8', 'rb') as f:
    compressed = f.read()

# Decompress it
with lzma.open('../data/xz/enwik8', 'rb') as f:
    decompressed = f.read()

# Check that the decompressed file is the same as the original
with open('../data/enwik8', 'rb') as f:
    original = f.read()
assert decompressed == original
 
# Test L
