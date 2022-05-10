import bz2
# Test BZ2Decompressor

dec = bz2.BZ2Decompressor()
data = open('sample.bz2', 'rb').read()
decompressed_data = dec.decompress(data)
print(decompressed_data)

# Test BZ2Compressor

comp = bz2.BZ2Compressor()
compressed_data = comp.compress(b'Hello World!')
compressed_data += comp.flush()
print(compressed_data)

# Test BZ2File

with bz2.BZ2File('sample.bz2', 'rb') as f:
    print(f.read())

with bz2.BZ2File('sample.bz2', 'wb') as f:
    f.write(b'Hello World!')

# Test BZ2Compressor.compress()

comp = bz2.BZ2Compressor()
compressed_data = comp.compress(b'Hello World!')
compressed_data += comp.flush()
print(compressed_data)

# Test B
