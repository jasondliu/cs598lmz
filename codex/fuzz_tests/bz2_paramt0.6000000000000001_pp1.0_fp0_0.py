from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(data)
#b'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'

# 内存中读写bytes
from io import BytesIO
f = BytesIO()
f.write(b'hello')
f.write(b' ')
f.write(b'world!')
f.getvalue()
#b'hello world!'

# StringIO操作的只能是str，如果要操作二进制数据，就需要使用BytesIO。

# 操作文件和目录
# 如果是posix，说明系统是Linux、Unix或Mac OS X
