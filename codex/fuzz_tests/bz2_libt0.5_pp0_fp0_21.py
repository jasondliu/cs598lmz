import bz2
bz2.compress(b"hello world")

# bz2.decompress(bz2.compress(b"hello world"))

import zlib
zlib.compress(b"hello world")

# zlib.decompress(zlib.compress(b"hello world"))

# 总结
# 压缩字符串
# 压缩字符串还有一个方法，就是使用pickle模块。
# pickle.dumps()方法把任意对象序列化成一个bytes，然后，就可以把这个bytes写入文件。或者用另一个方法pickle.dump()直接把对象序列化后写入一个file-like Object
