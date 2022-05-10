from lzma import LZMADecompressor
LZMADecompressor().decompress(src)

import bz2
bz2.decompress(src)

import zlib
zlib.decompress(src)



"""
实现一个你自己的字典类
"""
# 您可以定义一个名为 UserDict 的类来提供自己的字典类，
# 从而继承所有 Python 标准字典的行为。
# 使用它的好处是您不必再编写一些重复的代码来实现基
# 本的字典操作，这样您就可以把精力放在实现自己的
