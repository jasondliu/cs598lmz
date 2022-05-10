import bz2
# Test BZ2Decompressor

data = bz2.compress(b'Hello World')
print(data)

decompressor = bz2.BZ2Decompressor()
print(decompressor.decompress(data))

print(decompressor.decompress(data[:-1]))

print(decompressor.decompress(data[:-2]))

print(decompressor.decompress(data[:-3]))

print(decompressor.decompress(data[:-4]))

print(decompressor.decompress(data[:-5]))

print(decompressor.decompress(data[:-6]))

print(decompressor.decompress(data[:-7]))

print(decompressor.decompress(data[:-8]))

print(decompressor.decompress(data[:-9]))

print(decompressor.decompress(data[:-10]))

print(decompressor.decompress(data[:-11]))

print(decompressor
