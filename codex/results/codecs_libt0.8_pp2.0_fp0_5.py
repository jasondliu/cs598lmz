import codecs
codecs.open('unicode.txt', encoding='utf-8')

# 字节码

# 1字节码文件
b = bytes(3)
# 第一个参数为可迭代的bytes-like-objec，第二个参数为encoding，第三个参数为错误处理
b.decode('utf-8', 'strict')

# 2字节码模式
# 'b'表示二进制模式，传输文件时不会对内容进行编码转换
f = open('file.txt', mode='b', encoding='utf-8')

# 3字节码文件读取
with open('file.txt', mode
