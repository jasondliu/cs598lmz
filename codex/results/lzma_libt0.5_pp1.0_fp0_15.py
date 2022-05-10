import lzma
lzma.LZMA_OK

# 因为lzma模块不支持Python3，所以需要使用pylzma模块来替代
import pylzma
pylzma.LZMA_OK

# 创建一个压缩输出流，并将输出流写入lzma文件中
f = open('../tmp/test.lzma', 'wb')
c = pylzma.compressobj()
f.write(c.compress('Hello World'))
f.close()

# 使用pylzma模块的LZMADecompressor()方法来解压缩lzma文件
f = open('../tmp/test.lzma', 'rb')
d = pylzma.decompressobj()

