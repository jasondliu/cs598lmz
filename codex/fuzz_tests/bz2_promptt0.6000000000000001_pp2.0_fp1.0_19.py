import bz2
# Test BZ2Decompressor
import bz2

with open('data/sample.txt.bz2', 'rb') as f:
    with bz2.BZ2Decompressor() as decompressor:
        for data in iter(lambda: f.read(100 * 1024), b''):
            print(decompressor.decompress(data))

# Test BZ2File
with bz2.BZ2File('data/sample.txt.bz2', 'rb') as f:
    print(f.read().decode('utf-8'))

# Test BZ2Compressor
with open('data/sample.txt.bz2', 'rb') as f:
    with bz2.BZ2Compressor() as compressor:
        for data in iter(lambda: f.read(100 * 1024), b''):
            print(compressor.compress(data))

# Test BZ2File
with bz2.BZ2File('data/sample.txt.bz2', 'wb') as f:
    f.write(b'Hello World')
# Test L
