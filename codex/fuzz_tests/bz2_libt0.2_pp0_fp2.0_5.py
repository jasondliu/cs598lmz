import bz2
bz2.decompress(bz2.compress(b'hello world'))

# bz2.compress() 和 bz2.decompress() 函数分别对数据进行压缩和解压缩。
# 它们只接受单个的字节字符串作为输入和输出。
# 如果你想处理文件或者其他的二进制数据流，你可以使用 bz2.BZ2Compressor 和 bz2.BZ2Decompressor 类来包装一个流文件对象。
# 例如：
import bz2

with open('lorem.txt', 'rb') as input:

