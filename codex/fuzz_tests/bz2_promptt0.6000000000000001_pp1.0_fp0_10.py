import bz2
# Test BZ2Decompressor.decompress():
decompressor = bz2.BZ2Decompressor()
with open('output.bz2', 'rb') as f:
    while True:
        data = f.read(100)
        if not data:
            break
        else:
            print(decompressor.decompress(data))

# Test BZ2File:
with bz2.BZ2File('output.bz2', 'rb') as f:
    for line in f:
        print(line)

# Test compressing and decompressing with BZ2Compressor and BZ2Decompressor:
compressor = bz2.BZ2Compressor()
decompressor = bz2.BZ2Decompressor()

with open('output.bz2', 'wb') as f:
    f.write(compressor.compress(b'hello, world!'))
    f.write(compressor.flush())

with open('output.bz2', 'rb') as f:
    print(decompressor.decompress(f.read
