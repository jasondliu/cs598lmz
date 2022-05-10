import bz2
# Test BZ2Decompressor
d = bz2.BZ2Decompressor()
decompressed_data = d.decompress(data)
print(decompressed_data.decode('utf-8'))

# Test BZ2File
with bz2.BZ2File('file.bz2', 'wb') as f:
    f.write(data)
with bz2.BZ2File('file.bz2', 'rb') as f:
    print(f.read().decode('utf-8'))
