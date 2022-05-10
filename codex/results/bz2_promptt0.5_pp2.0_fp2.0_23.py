import bz2
# Test BZ2Decompressor

data = bz2.compress(bytes('This is a string', 'utf-8'))

decompressor = bz2.BZ2Decompressor()

try:
    print(decompressor.decompress(data))
except EOFError:
    print('Not enough data to decompress')

decompressor.decompress(data[0:1])
print(decompressor.unused_data)

try:
    print(decompressor.decompress(data[1:]))
except EOFError:
    print('Not enough data to decompress')

decompressor.decompress(data)
print(decompressor.unused_data)

# Test BZ2File

with bz2.BZ2File('lorem.txt.bz2', 'wb') as f:
    f.write(bytes('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec ac fringilla urna. In vulputate,', 'utf-8'))
    f.
