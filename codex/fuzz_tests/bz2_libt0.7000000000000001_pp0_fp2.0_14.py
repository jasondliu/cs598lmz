import bz2
bz2.decompress(data)

#bz2.BZ2Decompressor()

compressor = bz2.BZ2Decompressor()
chunks = []
for chunk in iter(lambda: file.read(100 * 1024), b''):
    chunks.append(compressor.decompress(chunk))

data = b''.join(chunks)


# 使用压缩文件
# with open('/tmp/spam.bz2', 'rb') as input:
#     with bz2.open(input, 'rt') as decompressor:
#         for line in decompressor:
#             ...


# 使用gzip压缩文件对象

import gzip
f = open('/tmp/spam.gz', 'rb')
with gzip.open(f, 'rt') as g:
    text = g.read()


# 反序列化
# json

import json
json.dumps(['foo', {'bar
