import bz2
# Test BZ2Decompressor

decompressor = bz2.BZ2Decompressor()

with open('data/enwik8.bz2', 'rb') as input, open('data/enwik8.txt', 'wb') as output:
    for block in iter(lambda: input.read(100 * 1024), b''):
        output.write(decompressor.decompress(block))
 
with open('data/enwik8.txt', 'rb') as f:
    text = f.read()
    print(text[:100])

# Test BZ2Compressor

compressor = bz2.BZ2Compressor()

with open('data/enwik8.txt', 'rb') as input, open('data/enwik8_compressed.bz2', 'wb') as output:
    for block in iter(lambda: input.read(100 * 1024), b''):
        output.write(compressor.compress(block))
    output.write(compressor.flush())

with open('data/enwik8_compressed.bz2', 'rb
