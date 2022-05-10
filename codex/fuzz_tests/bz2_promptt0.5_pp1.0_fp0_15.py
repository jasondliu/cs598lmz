import bz2
# Test BZ2Decompressor

with bz2.BZ2File('data/enwik8.bz2') as f:
    decompressor = bz2.BZ2Decompressor()
    text = decompressor.decompress(f.read(100000))
    print(text[:1000].decode('utf-8'))

with bz2.BZ2File('data/enwik8.bz2') as f:
    decompressor = bz2.BZ2Decompressor()
    text = decompressor.decompress(f.read(100000))
    print(text[:1000].decode('utf-8'))

# Test BZ2Compressor

compressor = bz2.BZ2Compressor()
compressed_data = compressor.compress(b'This is some data')
compressed_data += compressor.compress(b'and some more')
compressed_data += compressor.compress(b'and even more')
compressed_data += compressor.flush()

print(compressed_data)

# Test BZ2File

