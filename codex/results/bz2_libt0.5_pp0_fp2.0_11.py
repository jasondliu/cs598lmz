import bz2
bz2.compress(b'hello world!')

# 解压
bz2.decompress(b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084')

# 文件压缩
with bz2.BZ2File('file.bz2', 'w') as f:
    f.write(b'hello world!')

with bz2.BZ2File('file.bz2', 'r') as f:
    print(f.read())

# 压缩文件分块读取
with bz2.BZ2File('file.bz2') as f:
    for line in f:
        print(line)

# bz2.BZ2Compressor()
