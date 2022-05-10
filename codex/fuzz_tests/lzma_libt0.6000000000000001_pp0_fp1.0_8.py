import lzma
lzma.decompress(data).decode('utf-8')

# 二进制文件
# 二进制I/O函数
# open()的第二个参数是可选的，默认为'r'，可以是'rb'，'wb'，'ab'等
# 字节数组
data = bytes(range(0, 256))
with open('tmp/data.bin', 'wb') as f:
    f.write(data)

with open('tmp/data.bin', 'rb') as f:
    data = f.read()

# 字节数组的切片
data[0:10]

# 字节数组和整数序列的转换
# 整数序列转字
