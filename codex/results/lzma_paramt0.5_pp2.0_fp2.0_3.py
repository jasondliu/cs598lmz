from lzma import LZMADecompressor
LZMADecompressor().decompress(compressed_data)

# 可以使用lzma模块的open()函数来操作压缩或未压缩的LZMA文件
# 如果文件是未压缩的，open()函数就像是普通的open()函数
# 如果文件是压缩的，open()函数返回一个LZMAFile对象
import lzma
with lzma.open('foo.xz', 'rt') as f:
    print(f.read())

# 对于压缩的文件，可以传递一个format参数给open()函数来指定文件的压缩格式
