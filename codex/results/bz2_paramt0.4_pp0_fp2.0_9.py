from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2.BZ2File('../data/file.bz2').read())

# 如果你想对压缩数据进行迭代处理或者以块的方式来处理，可以使用
# BZ2Decompressor 对象，它不像 BZ2File() 函数那样一次性的解压数据源。
import bz2
dec = bz2.BZ2Decompressor()
for chunk in iter(lambda : file.read(100 * 1024), b''):
    rv = dec.decompress(chunk)
    if rv:
        process(rv)

# 如果你想使用压缩文件的上下文管理器，
