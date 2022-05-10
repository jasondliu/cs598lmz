import bz2
bz2.decompress(compressed)

# 压缩文件
with open('filename.txt', 'rb') as input:
    with bz2.BZ2File('filename.bz2', 'wb') as output:
        output.writelines(input)

# 解压文件
with bz2.BZ2File('filename.bz2', 'rb') as input:
    with open('filename.txt', 'wb') as output:
        output.writelines(input)

# 压缩数据并写入文件
with open('filename.txt', 'rb') as input:
    with bz2.BZ2File('filename.bz2', 'wb') as output:
        output.write(input.read())

# 解压文件并写入数据
with bz2.BZ2File('filename.bz2', 'rb') as input:
    with open('filename.txt', 'wb')
