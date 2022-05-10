import bz2
# Test BZ2Decompressor

buf = bz2.compress(b"hello world!")
buf2 = bz2.decompress(buf)
print(buf2)

print('=' * 20)

buf = bz2.compress(b"hello world!")
buf2 = b''
decompressor = bz2.BZ2Decompressor()
for i in range(len(buf)):
    buf2 += decompressor.decompress(buf[i:i + 1])
print(buf2)
print(decompressor.unused_data)

print('=' * 20)

buf = bz2.compress(b"hello world!")
buf2 = b''
decompressor = bz2.BZ2Decompressor()
for i in range(len(buf)):
    buf2 += decompressor.decompress(buf[i:i + 1])
print(buf2)
print(decompressor.unused_data)

print('=' * 20)

buf = bz2.compress(b"hello world!")
buf
