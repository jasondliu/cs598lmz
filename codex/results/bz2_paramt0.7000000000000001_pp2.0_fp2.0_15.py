from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2_data)

# 使用一个压缩的文件
# import bz2
# with bz2.open('file.bz2', 'rt') as f:
#     data = f.read()

# 创建压缩的文件
# with bz2.open('file.bz2', 'wt') as f:
#     f.write(data)

# 还有一个高级的压缩工具就是 bz2 模块中的 BZ2Compressor 和 BZ2Decompressor 类
# 可以用来处理大量的数据。
# 它们的使用方式非常的简单，但是需要你自己去分片和组装数
