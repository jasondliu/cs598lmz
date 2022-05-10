from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2.compress(b'hello world!'))

# 压缩文件
# 压缩文件的方式也很简单，只需要写入压缩后的数据即可。
#
# 写入压缩文件的时候，需要指定压缩模式，可以是 'w' 或 'x' ，后者表示如果压缩文件已存在则报错。
#
# 使用 'w' 模式写入压缩文件时，如果文件已存在，会直接覆盖。
#
