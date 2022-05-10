import bz2
bz2.BZ2Compressor().compress(b'hello world!')

# 压缩数据
data = bz2.compress(b'hello world!')
data

# 解压缩数据
bz2.decompress(data)

# 对文件压缩
with bz2.BZ2File('spam.bz2', 'w') as f:
    f.write(b'Hello World!')

with bz2.BZ2File('spam.bz2', 'r') as f:
    print(f.read())

# 压缩和解压缩文件
with open('lorem.txt', 'rb') as input:
    with bz2.BZ2File('lorem.bz2', 'wb') as output:
        output.writelines(input)

with bz2.BZ2File('lorem.bz2', 'rb') as input:
