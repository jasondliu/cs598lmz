from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

# 当然，你可以指定一个输出缓冲区来接收解压数据。
decompressor = LZMADecompressor()
decompressor.decompress(data, max_length=100)

# 你可以通过unused_data来获取输入数据中未使用的部分。
decompressor.unused_data

# 如果你想压缩或者解压一个文件，你可以使用LZMAFile类。
import lzma
with lzma.open('file.xz', 'rt') as f:
    text = f.read()

with lzma.open('file.xz', 'wt') as f:
   
