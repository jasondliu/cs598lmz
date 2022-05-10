from bz2 import BZ2Decompressor
BZ2Decompressor()

print(BZ2Decompressor().decompress(b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'))

# 使用bz2模块压缩数据
import bz2
data = b'hello world'
print(bz2.compress(data))
print(bz2.decompress(bz2.compress(data)))

# 压缩文件
import bz2
uncompressed_data = b'\x00\x00\x00\x00\x00\x00\x00\x00'
with bz2.BZ2File('file.bz2', 'wb') as f:
    f.write(uncompressed_data)

