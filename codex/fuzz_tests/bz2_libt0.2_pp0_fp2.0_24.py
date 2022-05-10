import bz2
bz2.decompress(bz2.compress(b'Hello World!'))

# bz2.compress() 和 bz2.decompress() 函数分别用于压缩和解压缩数据。
# 它们接受一个字节字符串作为输入，并返回一个字节字符串作为输出。
# 如果输入的字节字符串是不可压缩的，那么压缩后的输出长度可能会比输入长。
# 如果输入的字节字符串是经过
