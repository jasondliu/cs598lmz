import lzma
# Test LZMADecompressor

with lzma.open('lzma_compressed.lzma', 'rb') as input:
    decompressor = lzma.LZMADecompressor()
    with open('lzma_decompressed.txt', 'wb') as output:
        for block in iter(lambda: input.read(100 * 1024), b''):
            output.write(decompressor.decompress(block))
        output.write(decompressor.flush())
 
# LZMAFile

with lzma.open('lzma_compressed.lzma', 'rb') as input:
    with open('lzma_decompressed.txt', 'wb') as output:
        output.write(input.read())
 
# LZMADecompressor

with open('lzma_compressed.lzma', 'rb') as input:
    decompressor = lzma.LZMADecompressor()
    with open('lzma_decompressed.txt', 'wb') as output:
        for block in iter(lambda
