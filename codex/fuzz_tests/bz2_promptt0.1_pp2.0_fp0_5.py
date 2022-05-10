import bz2
# Test BZ2Decompressor

decompressor = bz2.BZ2Decompressor()

with open('data/enwik8.bz2', 'rb') as f:
    data = f.read(100)
    while data:
        print(decompressor.decompress(data))
        data = f.read(100)

print(decompressor.decompress(b'\x00\x00\x00\x00'))

print(decompressor.unused_data)

print(decompressor.eof)

print(decompressor.needs_input)

print(decompressor.unused_data)

print(decompressor.eof)

print(decompressor.needs_input)

print(decompressor.unused_data)

print(decompressor.eof)

print(decompressor.needs_input)

print(decompressor.unused_data)

print(decompressor.eof)

print(decompressor.needs_input)

print(decompressor
