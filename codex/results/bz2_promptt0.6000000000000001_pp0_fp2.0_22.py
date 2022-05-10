import bz2
# Test BZ2Decompressor

data = bz2.compress(b'*' * 100)

print(len(data))

decompressor = bz2.BZ2Decompressor()
print(decompressor.decompress(data))

print(decompressor.decompress(data[:4]))
print(decompressor.decompress(data[4:8]))
print(decompressor.decompress(data[8:12]))

print(decompressor.decompress(data[:-4]))
print(decompressor.decompress(data[-4:]))

print(len(decompressor.decompress(data + b'a')))

print(len(decompressor.decompress(data + b'a', 1)))

try:
    decompressor.decompress(b'a')
except ValueError as e:
    print(e)

try:
    decompressor.decompress(data, 1)
except ValueError as e:
    print(e)

try:
    decompressor
