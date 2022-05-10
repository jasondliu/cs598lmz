import socket
socket.if_indextoname("1")

# 3.2.1
# b = bytes("hello,world", "ascii")
# print(b)
# c = b.decode("ascii")
# print(c)

# d = "中文".encode("utf-8")
# print(d)
# e = d.decode("utf-8")
# print(e)

# 3.2.2 文本对象和字节对象之间的转换
# a = "中文".encode("utf-8")
# print(a)
# b = a.decode("utf-8")
# print(b)

# 3.2.3 使用编码的编解码器
# f = open("unicode.txt", "w", encoding="utf-8")
# f.write(b"中文")
# f.close()

# f = open("unicode.txt",
