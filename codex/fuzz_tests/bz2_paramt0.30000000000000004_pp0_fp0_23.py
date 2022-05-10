from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2_data)

# 压缩
import bz2
uncompressed_data = b'Welcome to the Idiot\'s Guide to Compression!'
compressed_data = bz2.compress(uncompressed_data)
compressed_data

# 解压缩
bz2.decompress(compressed_data)

# 压缩文件
with open('filename.txt', 'rb') as input:
    with bz2.open('filename.txt.bz2', 'wb') as output:
        output.writelines(input)

# 解压缩文件
with bz2.open('filename.txt.bz2', 'rb') as input:
    with open('filename.txt', 'wb') as output:
        for line in input:
            output.write(line)

# 压缩文件
import bz2
with open('filename.txt', 'rb') as input:
    bz_comp
