import bz2
bz2.decompress(bz2.compress(b'hello'))

# 将压缩数据写入文件
with bz2.BZ2File('test.bz2', 'w') as f:
    f.write(b'hello world')

# 读取压缩文件
with bz2.BZ2File('test.bz2') as f:
    print(f.read())

# 压缩文件和普通文件一样，可以用seek()和tell()方法
with bz2.BZ2File('test.bz2') as f:
    print(f.tell())
    print(f.seek(3))
    print(f.read(1))
    print(f.seek(0))
    print(f.read(9))

# 压缩文件还可以用for
