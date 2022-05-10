import bz2
bz2file = bz2.BZ2File(bz2filename)
try:
    for line in bz2file:
        print(line)
finally:
    bz2file.close()

# 内存中解压缩
import bz2
compressed_data = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
decompressed = bz2.decompress(compressed_data)
print(decompressed)

# 压缩的块大小
import bz2
bz2_compressor = bz2.BZ2Compressor()
result = bz2_compressor.compress(b'Hello')
print(result)
print(bz2_compressor.flush())
