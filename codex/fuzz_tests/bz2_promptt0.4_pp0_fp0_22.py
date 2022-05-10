import bz2
# Test BZ2Decompressor

decompressor = bz2.BZ2Decompressor()

with open('data/enwik9.bz2', 'rb') as f:
    while True:
        chunk = f.read(1024)
        if not chunk:
            break
        decompressed_chunk = decompressor.decompress(chunk)
        print(decompressed_chunk)
        break

print(decompressor.unused_data)

# Test BZ2File

with bz2.BZ2File('data/enwik9.bz2', 'rb') as f:
    for line in f:
        print(line)
        break

# Test BZ2Compressor

compressor = bz2.BZ2Compressor()

with open('data/enwik9.bz2', 'rb') as f:
    while True:
        chunk = f.read(1024)
        if not chunk:
            break
        compressed_chunk = compressor.compress(chunk)
        print(compressed_chunk)
        break
