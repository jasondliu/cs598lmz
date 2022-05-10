import bz2
# Test BZ2Decompressor

try:
    bz2decompressor = bz2.BZ2Decompressor()
except:
    print("SKIP")
    raise SystemExit

data = bz2.compress(b"hello")
print(bz2decompressor.decompress(data))
print(bz2decompressor.decompress(data))
print(bz2decompressor.decompress(data))
print(bz2decompressor.decompress(data, 1))
print(bz2decompressor.decompress(data, 1))
print(bz2decompressor.decompress(data, 1))
print(bz2decompressor.decompress(data, 1))
print(bz2decompressor.decompress(data, 1))
print(bz2decompressor.decompress(data, 1))
print(bz2decompressor.decompress(data, 1))
print(bz2decompressor.decompress(data, 1))
print(bz2decompressor.
