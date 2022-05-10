import bz2
bz2.decompress(bz2.compress(b'hello world!'))

# 标准库中的bz2模块还提供了一个BZ2Compressor和BZ2Decompressor类，可以用于更底层的控制
# 压缩数据
compressor = bz2.BZ2Compressor()
compressor.compress(b'hello world!')
compressor.flush()
# 解压缩数据
decompressor = bz2.BZ2Decompressor()
decompressor.decompress(b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe
