import bz2
bz2.decompress(base64.b64decode('BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'))

# 打开压缩文件
f = bz2.BZ2File('example.bz2')
# 读取压缩文件
print(f.read())

# 写入压缩文件
f = bz2.BZ2File('example.bz2', 'w')
f.write(b'hello world')
f.close()

# 压缩和解压
import bz2
un = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01
