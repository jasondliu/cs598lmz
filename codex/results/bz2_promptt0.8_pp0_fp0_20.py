import bz2
# Test BZ2Decompressor

decompressor = bz2.BZ2Decompressor()

with bz2.open('source.bz2', 'rb') as source, open('source.txt', 'wb') as dest:
    for data in iter(lambda : source.read(100 * 1024), b''):
        decompressed = decompressor.decompress(data)
        if decompressed:
            dest.write(decompressed)
        else:
            print('buffering...')
# Test BZ2File

with bz2.BZ2File('source.bz2', 'rb') as compressed:
    with open('source.txt', 'wb') as decompressed:
        while True:
            data = compressed.read()
            if not data:
                break
            decompressed.write(data)
 
# decompressed.txt is the same as BZ2Decompressor
 
# Note: BZ2File can also write
 
# Compressing and decompressing with BZ2File is about 40% slower than using BZ2Compressor and BZ2Decompressor.

