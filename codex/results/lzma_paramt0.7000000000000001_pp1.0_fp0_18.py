from lzma import LZMADecompressor
LZMADecompressor(format=FORMAT_AUTO).decompress(b'\xfd7zXZ\x00\x00\x04\xe6\xd6\xb4F\x02\x00!\x01\x16\x00\x00\x00t/\x00\x00\x00\x00')

# write file
path = 'data/'
name = 'test'

with open(path + name + '.txt', 'wb') as f:
    f.write(b'\xfd7zXZ\x00\x00\x04\xe6\xd6\xb4F\x02\x00!\x01\x16\x00\x00\x00t/\x00\x00\x00\x00')

# uncompress file
with lzma.open(path + name + '.txt') as f:
    file_content = f.read()

print(file_content)

# compress file
with lzma.open(path + name + '_compress.txt', "w") as f
