import bz2
# Test BZ2Decompressor
with bz2.BZ2File('data/sample.bz2') as f:
    decompressor = bz2.BZ2Decompressor()
    for block in iter(lambda: f.read(100 * decompressor.decompress(b'\x00' * 100)), b''):
        print(decompressor.decompress(block).decode('utf-8'))

# Test BZ2Compressor
with bz2.BZ2File('data/sample.bz2', 'w') as f:
    compressor = bz2.BZ2Compressor()
    for data in ['Line 1', 'Line 2', 'Line 3']:
        f.write(compressor.compress(data.encode('utf-8')))
    f.write(compressor.flush())

# Test BZ2File.readlines()
with bz2.BZ2File('data/sample.bz2') as f:
    print(f.readlines())

# Test BZ2File.writelines()
with bz2.BZ
