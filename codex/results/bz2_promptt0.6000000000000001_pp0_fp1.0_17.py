import bz2
# Test BZ2Decompressor

decompressor = bz2.BZ2Decompressor()

with open('../data/enwik8.bz2', 'rb') as f:
    next_chunk = f.read(100)
    while next_chunk:
        print(decompressor.decompress(next_chunk), end='')
        next_chunk = f.read(100)

print(decompressor.decompress(b'\x00\x00\x00\x00'))

print(decompressor.unused_data)

print(decompressor.eof)

print(decompressor.needs_input)

print('\n' + decompressor.decompress(b''))

print(decompressor.eof)

print(decompressor.needs_input)

print('\n' + decompressor.flush())

print(decompressor.eof)

print(decompressor.needs_input)

print(decompressor.unconsumed_tail)

# Test BZ2
