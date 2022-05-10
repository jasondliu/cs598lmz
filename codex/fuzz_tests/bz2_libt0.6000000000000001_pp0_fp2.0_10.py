import bz2
bz2.decompress(bz2_data)

# 压缩文件
with open('file.txt', 'rb') as input:
    bz2_data = bz2.compress(input.read())
with open('file.bz2', 'wb') as output:
    output.write(bz2_data)

with bz2.open('file.bz2', 'rb') as input:
    print(input.read())

with bz2.open('file.txt.bz2', 'wt') as output:
    output.write('Contents of the example file go here.\n')

with bz2.open('file.txt.bz2', 'rt') as input:
    print(input.read())
