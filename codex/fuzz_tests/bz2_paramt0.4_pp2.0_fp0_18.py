from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2_data)

# 压缩数据
data = b'Lots of data here.'
bz2_data = bz2.compress(data)
bz2_data

# 压缩率
len(data)
len(bz2_data)

# 解压
bz2.decompress(bz2_data)

# 压缩文件
with open('file.txt', 'rb') as input:
    data = input.read()
with open('file.bz2', 'wb') as output:
    output.write(bz2.compress(data))

# 解压文件
with open('file.bz2', 'rb') as input:
    print(bz2.decompress(input.read()))

# 压缩文件
with bz2.BZ2File('file.bz2', 'wb') as output:
    output.write(data
