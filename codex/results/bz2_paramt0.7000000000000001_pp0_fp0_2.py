from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(compressed_data)

# 或者
from bz2 import decompress
decompress(compressed_data)

# 如果你有一个大型的压缩数据块，可以使用一个 BZ2Decompressor 对象来解压数据流
decompressor = BZ2Decompressor()
decompressor.decompress(chunk1)
decompressor.decompress(chunk2)

# 如果你想在压缩数据上使用一些高级的操作，比如对数据流进行迭代以便处理大文件，你可以使用 BZ2File() 函数来创建一
