import bz2
# Test BZ2Decompressor
with bz2.BZ2File(fn, 'r') as f:
    decompressor = bz2.BZ2Decompressor()
    f.read(1)
    print(decompressor.decompress(b'BZ'))
    f.read(2)
    print(decompressor.decompress(b'h\x9c'))
    f.read(1)
    print(decompressor.decompress(b'\x00'))
    f.read(2)
    print(decompressor.decompress(b'\x00\x01'))
    f.read(1)
    print(decompressor.decompress(b'\x04'))
    f.read(1)
    print(decompressor.decompress(b'\x00'))
    f.read(1)
    print(decompressor.decompress(b'\x00'))
    f.read(1)
    print(decompressor.decompress(b'\x00'))

