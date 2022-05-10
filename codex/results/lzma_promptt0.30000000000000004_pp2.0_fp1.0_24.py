import lzma
# Test LZMADecompressor
compressor = lzma.LZMADecompressor()
with open('data/enwik8', 'rb') as input, open('data/enwik8.out', 'wb') as output:
    while True:
        block = input.read(1024)
        if not block:
            break
        output.write(compressor.decompress(block))
    output.write(compressor.flush())

# Test LZMACompressor
compressor = lzma.LZMACompressor()
with open('data/enwik8', 'rb') as input, open('data/enwik8.xz', 'wb') as output:
    while True:
        block = input.read(1024)
        if not block:
            break
        output.write(compressor.compress(block))
    output.write(compressor.flush())
 
# Test LZMAFile
with lzma.open('data/enwik8.xz', 'rb') as input, open('data/enwik8.out', 'wb') as output:
    output.write
