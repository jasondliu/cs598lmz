from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084')

# 使用上下文管理器
with BZ2File('file.bz2', 'wb') as f:
    f.write(b'hello world')

with BZ2File('file.bz2', 'rb') as f:
    print(f.read())

# 压缩文件
import bz2
uncompressed = b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\t\n\x0b\x0c\r\x0e\x0f\x10\x11\x12\x13\x14\x15\
