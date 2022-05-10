import bz2
bz2.decompress(bz2_data)

# 使用bz2.BZ2File()来读取bz2文件
with bz2.BZ2File('example.bz2') as f:
    print(f.read())

# 压缩数据
with open('example.txt', 'rt') as f:
    data = f.read()

with bz2.BZ2File('example.bz2', 'wt') as f:
    f.write(data)

# 压缩数据并写入文件
with open('example.txt', 'rt') as input:
    with bz2.BZ2File('example.bz2', 'wt') as output:
        output.writelines(input)

# 压缩数据并写入文件
with open('example.txt', 'rt') as input:
    with bz2.BZ2File('example
