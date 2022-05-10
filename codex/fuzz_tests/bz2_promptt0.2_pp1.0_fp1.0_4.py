import bz2
# Test BZ2Decompressor

bz2_decompressor = bz2.BZ2Decompressor()

with open('data/enwik8.bz2', 'rb') as f:
    file_content = f.read()
    print(file_content[:10])
    print(bz2_decompressor.decompress(file_content)[:10])

# Test BZ2File

with bz2.BZ2File('data/enwik8.bz2', 'rb') as f:
    print(f.read(10))

# Test BZ2Compressor

bz2_compressor = bz2.BZ2Compressor()

with open('data/enwik8.bz2', 'rb') as f:
    file_content = f.read()
    compressed_content = bz2_compressor.compress(file_content)
    print(compressed_content[:10])
    print(bz2.decompress(compressed_content)[:10])

# Test BZ2File

with bz
