from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2.compress(b"hello world!"))





# 3、 python 提供一个BZIP2的压缩扩展
import bz2
f = open('file.txt','wb')
f.write(b"This is a test")
f.close()

f1 = bz2.BZ2File('file.txt.bz2','wb')
f1.write(b"This is a test")
f1.close()

f2 = open('file.txt.bz2','rb')
f2.read()

f3 = bz2.BZ2File('file.txt.bz2','rb')
f3.read()


f4 = open('file.txt.bz2','wb')
f5 = bz2.BZ2File('file.txt.bz2','wb')

import sys
f4.write(b"this is a test \n"*1000)
f4.close()

f5.write(b"
