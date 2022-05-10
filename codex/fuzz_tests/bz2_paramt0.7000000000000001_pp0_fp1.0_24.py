from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(s)

s = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
print(BZ2Decompressor().decompress(s))

print(BZ2Decompressor(s).decompress(s))

import bz2
print(bz2.decompress(s))

# 当然，我们也可以直接使用 BZ2File 解压文件
with bz2.BZ2File('file.bz2') as f:
    file_content = f.read()
