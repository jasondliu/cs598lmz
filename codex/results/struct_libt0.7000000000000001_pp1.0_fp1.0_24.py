import _struct
print _struct.calcsize('=hhl')
print _struct.unpack('=hhl', "abcd1234")

# ! 为网络字节序
print _struct.pack('!hhl', 1, 2, 3)

# > 大端字节序
# < 小端字节序
print _struct.pack('>hhl', 1, 2, 3)
print _struct.pack('<hhl', 1, 2, 3)
