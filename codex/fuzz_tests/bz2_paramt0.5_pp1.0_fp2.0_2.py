from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2_data)

# 使用bz2.open()代替open()
with bz2.open('somefile.bz2', 'wt') as f:
    f.write(text)

# 压缩文件
with open('somefile.txt', 'rb') as input:
    with bz2.open('somefile.bz2', 'wb') as output:
        output.write(input.read())

# 解压缩文件
with bz2.open('somefile.bz2', 'rb') as input:
    with open('somefile.txt', 'wb') as output:
        for line in input:
            output.write(line)

# 压缩文件，每次读取一行
import bz2
uncompressed_data = b'\n'.join(lines)
len(uncompressed_data)

compressed_data = bz2.compress
