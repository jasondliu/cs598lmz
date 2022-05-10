import lzma
# Test LZMADecompressor.
#每次回调函数执行后，应该返回的数据长度
uncompressed_data_target = 100000

#压缩数据
cdata = lzma.compress(bytes([x % 256 for x in range(uncompressed_data_target)]))

#获取解压缩对象
lzc = lzma.LZMADecompressor()

#输入数据
data = b''
#输出数据
d = b''

#还要输入的数据数量
input_remaining = len(cdata)
print(input_remaining)

#输出的数据数量
output_remaining = uncompressed_data_target

