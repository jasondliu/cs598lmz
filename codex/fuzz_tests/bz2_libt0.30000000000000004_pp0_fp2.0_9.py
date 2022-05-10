import bz2
bz2.compress(b'hello world')

bz2.decompress(b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084')

# bz2.compress()和bz2.decompress()只处理bytes类型

# 如果要处理文本文件，可以先用open()函数读取文件内容，再传入bz2.compress()
# 或bz2.decompress()，这样就不必处理编码问题

# 压缩文件

