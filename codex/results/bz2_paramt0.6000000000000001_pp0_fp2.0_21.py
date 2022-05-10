from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(data)

# 7. 使用适配器类
import io
import bz2
un = bz2.BZ2Decompressor()
f = open('sample.bz2')
bz_file = io.BufferedReader(f)
data = bz_file.read(100)
un.decompress(data)

# 8. 字节字符串操作
data = b'Hello World'
data[0:5]
data.startswith(b'Hello')
data.split()
data.replace(b'Hello', b'Hello Cruel')

# 9. 使用正则表达式匹配字节字符串
data = b'FOO:BAR,SPAM'
import re
re.split('[:,]', data)
re.split('(:|,)', data)

# 10. 打印输出字
