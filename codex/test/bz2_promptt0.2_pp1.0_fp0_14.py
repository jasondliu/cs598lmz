import bz2
# Test BZ2Decompressor

data = bz2.compress(b"this is a test")
print(data)

decompressor = bz2.BZ2Decompressor()

try:
    print(decompressor.decompress(data))
except EOFError:
    print("Cannot decompress data; data may be truncated")

