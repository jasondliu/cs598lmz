import bz2
# Test BZ2Decompressor
with bz2.BZ2Decompressor() as decompressor:
    print('Repr:', repr(decompressor))
    decompressor.decompress(b'BZh91AY&SY')
    decompressor.decompress(b'Ao')
    decompressor.decompress(b'LCAAAAA')
    decompressor.decompress(b'Ao')
    decompressor.decompress(b'LCAAAAA')
    decompressor.decompress(b'Ao')
    decompressor.decompress(b'LCAAAAA')
    decompressor.decompress(b'Ao')
    decompressor.decompress(b'LCAAAAA')
    decompressor.decompress(b'Ao')
    decompressor.decompress(b'LCAAAAA')
    decompressor.decompress(b'Ao')
    decompressor.decompress(b'LCAAAAA')
    decompressor.decompress(b'Ao')
    decompressor.decompress(b'LCAAAAA')
    decomp
