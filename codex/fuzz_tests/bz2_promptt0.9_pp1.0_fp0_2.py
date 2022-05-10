import bz2
# Test BZ2Decompressor and BZ2Compressor classes

data = b'\x42\x5a\x68\x39\x31\x41\x59\x26\x53\x59'
d = bz2.decompressobj()
print(d.decompress(data))

print('******************')
