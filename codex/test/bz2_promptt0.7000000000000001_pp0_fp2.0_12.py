import bz2
# Test BZ2Decompressor and BZ2Compressor
with bz2.BZ2File('lorem.txt.bz2') as source, open('lorem.out', 'wb') as target:
    decompressor = bz2.BZ2Decompressor()
    while True:
        block = source.read(1024)
        if not block:
            break
        target.write(decompressor.decompress(block))
