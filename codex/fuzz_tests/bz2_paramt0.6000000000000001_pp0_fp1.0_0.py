from bz2 import BZ2Decompressor
BZ2Decompressor(filename='test.bz2')

# 字节到文本
# 如果你读取二进制数据到一个变量中去，那么解码是很简单的事情。比如：
import array
numbers = array.array('h', [-2, -1, 0, 1, 2])
octets = bytes(numbers)
print(octets)

# 要把这些字节值解码为一个文本字符串，你必须调用 str() 函数给它们传递编码过程的名称。比如：
print(str(octets, encoding='utf-8'))

#
