from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2.BZ2File('foo.txt.bz2').read())

# 在很多情况下，你可能需要为每个操作设置一个压缩级别或其他参数。 
# 对于更高级的控制， 可以实例化一个 BZ2Compressor 和 BZ2Decompressor
import bz2
compressor = bz2.BZ2Compressor(9) # 9 is the compress level
compressor.compress(data)
compressor.flush()

decompressor = bz2.BZ2Decompressor()
decompressor.decompress(data)

# 对于压缩和解压缩，可以使用文
