import bz2
bz2.decompress(bz2.compress(b'hello world'))

# 压缩文件
with bz2.BZ2File('example.bz2', 'wb') as output:
    with open('example.txt', 'rb') as input:
        output.write(input.read())

# 解压文件
with bz2.BZ2File('example.bz2', 'rb') as input:
    with open('example.txt', 'wb') as output:
        output.write(input.read())

# 压缩文件
with bz2.open('example.bz2', 'wt') as output:
    output.write('Contents of the example file go here.\n')

# 解压文件
with bz2.open('example.bz2', 'rt') as input:
    print(input.read())

# 压缩文件
with bz2.open('example.bz2', 'wt
