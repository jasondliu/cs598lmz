from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(open('test.bz2','rb').read()).decode()

# 使用 gzip 模块
import gzip
