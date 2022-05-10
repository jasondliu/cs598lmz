import bz2
# Test BZ2Decompressor
with open('data/random_bytes.bin.bz2', 'rb') as f:
    compressed = f.read()

with bz2.BZ2Decompressor() as decompressor:
    with open('data/random_bytes.bin', 'wb') as f:
        f.write(decompressor.decompress(compressed))

with open('data/random_bytes.bin', 'rb') as f:
    data = f.read()

len(data)

with bz2.BZ2Decompressor() as decompressor:
    try:
        decompressor.decompress(data)
    except EOFError as e:
        print(e)

# Test BZ2Compressor
with open('data/random_bytes.bin', 'rb') as f:
    data = f.read()

with bz2.BZ2Compressor() as compressor:
    compressed = compressor.compress(data)
    compressed += compressor.flush()

len(compressed)

with open('data/random_bytes.bin.b
