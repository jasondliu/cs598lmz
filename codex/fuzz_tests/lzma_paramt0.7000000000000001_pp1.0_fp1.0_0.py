from lzma import LZMADecompressor
LZMADecompressor().decompress(packed)

from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(packed)

from zlib import decompress
decompress(packed)


'''
如果你想执行通用的压缩操作，但是又不想去依赖第三方的压缩库的话，可以使用 zlib 模块。 
它有着相同的压缩解压 API ，但是它并不能像那些模块那样提供高压缩率。例如：
'''
import zlib

original_data = b'This is the original text.'
print('Original   :', len(original_data), original_data)

