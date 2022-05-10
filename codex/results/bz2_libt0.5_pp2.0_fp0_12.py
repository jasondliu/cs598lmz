import bz2
bz2.decompress('BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084')

# 将压缩文件写入压缩文件
data = 'this is the data to write to the file.'
with bz2.BZ2File('data.bz2', 'w') as f:
    f.write(data)

# 将压缩文件写入内存
with bz2.BZ2File('data.bz2') as f:
    print(f.read())

# 将压缩文件写入压缩文件
with bz2.BZ2File('data.bz2', 'r
