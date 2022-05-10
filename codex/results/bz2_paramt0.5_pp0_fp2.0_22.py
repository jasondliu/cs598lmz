from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2data)

# 压缩
bz2.compress(data)

# 压缩文件
with open('file.txt', 'rb') as input:
    with bz2.BZ2File('file.bz2', 'wb') as output:
        output.write(input.read())

# 解压缩文件
with bz2.BZ2File('file.bz2', 'rb') as input:
    with open('file.txt', 'wb') as output:
        output.write(input.read())

# 压缩文件
bz2.compress(data, compresslevel=9)

# 结合gzip和bz2
import gzip
import bz2
for filename in ['file.txt', 'file.txt.gz', 'file.txt.bz2']:
    print(filename)
    with open(filename, 'rt') as input:
        print(input.read())
