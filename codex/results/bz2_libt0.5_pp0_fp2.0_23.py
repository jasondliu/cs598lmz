import bz2
bz2.compress(b"hello world")

# bz2.decompress(b'BZh91AY&SY\xc4\x98\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08')

# 压缩文件
# 压缩文件对象支持上下文语法:
with bz2.BZ2File('compress.bz2', 'w') as f:
    f.write(b'hello world')

# 解压缩文件
with bz2.BZ2File('compress.bz2', 'r') as f:
    data = f.read()
    print(data)
