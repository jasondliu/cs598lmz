import bz2
bz2.decompress(bz2.compress(b'hello world'))

# bz2.compress() 和 bz2.decompress() 函数分别对字节串进行压缩和解压缩。
# 它们的参数是一个字节串，返回值也是一个字节串。

# 压缩和解压缩的过程是可逆的，所以可以把压缩后的字节串保存到文件中，
# 再把它读取出来解压缩。

# 压缩文件
with open('/tmp/example.txt', 'rb') as input:
