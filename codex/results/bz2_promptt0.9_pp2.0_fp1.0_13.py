import bz2
# Test BZ2Decompressor
with bz2.BZ2File('compressed.bz2', 'wb') as compressed:
    with open('input.txt', 'rb') as uncompressed:
        compressed.write(uncompressed.read())
# bz2.compress('Compressing a file using bz2')
compressor = bz2.BZ2Compressor(9)
with open('input.txt', 'rb') as uncompressed, open('compressed.bz2', 'wb') as compressed:
    while True:
        block = uncompressed.read(1024)
        if not block:
            break
        compressed.write(compressor.compress(block))
    compressed.write(compressor.flush())
# bz2.decompress('bz2.decompress(CompressedString)')
# Change the extension of the file from .bz2 to .py and run the file.
with bz2.BZ2File('compressed.bz2', 'rb') as compressed:
    with open('input.txt', 'wb') as uncompressed:
        uncompressed.write
