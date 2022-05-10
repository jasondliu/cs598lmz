from lzma import LZMADecompressor
LZMADecompressor.decompress(lzma_data)

# b'hello'

# 7.9 直接迭代
# 如果删除一个文件夹，且这个文件夹很大，可能会需要迭代处理文件夹中的
# 内容，然后删除。
# 下面的方法可能会有点慢，创建并删除较多的迭代对象。
import os
for root, dirs, files in os.walk('python/Lib/email'):
    for name in files:
        os.unlink(os.path.join(root, name))
    for name in dirs:
        os.rmdir(os.path.join(root, name))

# 一
