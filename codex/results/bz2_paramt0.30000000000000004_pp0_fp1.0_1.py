from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(compressed_data)

# bz2.decompress(compressed_data) # 也可以

# 压缩文件
# 可以使用bz2.open()来代替open()来打开一个bz2压缩文件，并且可以同时使用文件对象的方法读取或写入数据
with bz2.open('file.bz2', 'wt') as f:
    f.write(text)

with bz2.open('file.bz2', 'rt') as f:
    print(f.read())

# 压缩文件的一个缺点是它不能被随机访问。如果你想查找压缩文
