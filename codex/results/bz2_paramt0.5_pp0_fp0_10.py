from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084')

# 内存中压缩
import bz2
compressor = bz2.BZ2Compressor()
compressor.compress(b'i love python')
compressor.compress(b'i also love ruby')
compressor.flush()

# 压缩文件
import bz2
with open('filename.txt', 'rb') as input:
    with bz2.open('filename.txt.bz2', 'wb') as output:
        output.writelines(input)

# 解压文件
import bz2
with bz2.open('filename.txt.bz2', 'rb') as input:
   
