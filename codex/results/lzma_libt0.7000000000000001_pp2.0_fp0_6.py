import lzma
lzma.LZMACompressor().compress(b'foobar')

# Compress a file
import lzma
with open('data.out', 'wb') as f:
    compressor = lzma.LZMACompressor()
    for data in datagen():
        f.write(compressor.compress(data))
    f.write(compressor.flush())

# Decompress a file
import lzma
with open('data.xz', 'rb') as f:
    decompressor = lzma.LZMADecompressor()
    data = f.read(1024)
    while data:
        print(decompressor.decompress(data))
        data = f.read(1024)

# Decompress a file
import lzma
with open('data.xz', 'rb') as f:
    data = f.read()
    print(lzma.LZMADecompressor().decompress(data))

# Decompress a file
import lzma
with open('data.xz', 'rb
