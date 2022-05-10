import bz2
# Test BZ2Decompressor
bz2decompressor = bz2.BZ2Decompressor()
text = bz2decompressor.decompress(bz2compressed_text)
print(text)

text = bz2decompressor.decompress(bz2compressed_text)
print(text)

# Test BZ2File
bz2file = bz2.BZ2File('bz2compressed_text.bz2')
print(bz2file.read())

bz2file.seek(0)
print(bz2file.read())

bz2file.seek(0)
print(bz2file.read(15))

bz2file.seek(0)
print(bz2file.readline())

bz2file.seek(0)
print(bz2file.readlines())

with bz2.open('bz2compressed_text.bz2') as bz2file:
    print(bz2file.read())

# Test BZ2Compressor
b
