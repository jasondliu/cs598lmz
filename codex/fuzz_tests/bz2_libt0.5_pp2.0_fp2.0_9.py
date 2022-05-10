import bz2
bz2.decompress(b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084')

# 强制使用单字节模式去压缩文本
data = '这是一个测试字符串'
bz2.compress(data.encode('utf-8'))
bz2.compress(data.encode('utf-8'), 9)

# 使用bz2.BZ2Compressor对象
compressor = bz2.BZ2Compressor()
compressor.compress(data.encode('utf-8'))
compressor.flush()

# 使用bz2.BZ2Decompressor
