import bz2
# Test BZ2Decompressor
data = open('lorem.txt', 'rb').read()
compressor = bz2.BZ2Compressor()
compressed = compressor.compress(data)
compressed += compressor.flush()
decompressor = bz2.BZ2Decompressor()
decompressed = decompressor.decompress(compressed)
print(decompressed)

# Test BZ2File
with open('lorem.txt', 'rb') as input:
    with bz2.BZ2File('lorem.txt.bz2', 'wb') as output:
        output.write(input.read())

with bz2.BZ2File('lorem.txt.bz2', 'rb') as input:
    print(input.read())
