import lzma
lzma.decompress(b'\xfd7zXZ\x00\x00\x04\xe6\xd6\xb4F\x02\x00!\x01\x16\x00\x00\x00t/\xca\xccK(I\xcdI\x01\x00\x00\x04\xe6\xd6\xb4F')

#解压文件
import lzma
with lzma.open('lzma_compress.xz') as f:
    file_content = f.read()

#使用bz2压缩
import bz2
original_data = b'This is the original text.'
print('Original     :', len(original_data), original_data)
compressed = bz2.compress(original_data)
print('Compressed   :', len(compressed), compressed)
decompressed = bz2.decompress(compressed)
print('Decompressed :', len(decompressed), decompressed)

