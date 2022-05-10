from lzma import LZMADecompressor
LZMADecompressor().decompress(lzma_data)

# 字节数组
bdata = bytes(range(0, 256))
len(bdata)

bdata[0:10]

bdata[16:24]

bdata.startswith(b'\x10\x11\x12')

bdata.split(b'\x10\x11\x12')

# 字节数组的格式化字符串
bdata.replace(b'\x41', b'\x00')

b'{:10s} {:10d} {:10.2f}'.format(b'ACME', 100, 490.1)

# 字节数组的编解码
b'\x41\x42\x43\x44'.decode('ascii')

b'Hello World'.decode('ascii')

b'\x41\x42\x43\x
