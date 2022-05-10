import bz2
# Test BZ2Decompressor

with open('data/test.bz2', 'rb') as f:
    decompressor = bz2.BZ2Decompressor()
    for block in iter(lambda: f.read(100 * 1024), b''):
        print(decompressor.decompress(block))
# Test BZ2File

with bz2.BZ2File('data/test.bz2') as f:
    print(f.read())
 
 
# Test compress()

print(bz2.compress(b'hello world!'))
 
 
# Test decompress()

print(bz2.decompress(b'BZh91AY&SY\xd8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x
