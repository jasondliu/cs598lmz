import bz2
# Test BZ2Decompressor
from bz2 import BZ2Decompressor

sample_file = bz2.open('./data/sample.bz2', mode='wt')
sample_file.write('Contents go here')
sample_file.close()

with bz2.open('sample.bz2', mode='rt') as f:
    data = f.read()
    print(data)

decompressor = BZ2Decompressor()

with open('sample.bz2', 'rb') as f:
    file_content = f.read()
    # Decompress the compressed file content
    print(decompressor.decompress(file_content))


import zlib
s = b'witch which has which witches wrist watch'
print(len(s))

t = zlib.compress(s)
print(len(t))

zlib.decompress(t)

zlib.crc32(s)

# 自定义压缩
import struct

def compress(data):
    value = zlib.
