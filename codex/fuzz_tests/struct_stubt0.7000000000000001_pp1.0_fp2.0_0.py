from _struct import Struct
s = Struct.__new__(Struct)
print(s.format)

print('\n# 运算符重载')
print(struct.calcsize('P') * 8)
print(struct.pack('P', 10240099))
print(struct.unpack('P', b'\x00\x9c@c')[0]) #P是指针类型，针对64位操作系统，用8个字节存储地址

print('\n# 大量的数据')
with open('binary_file.bin', 'wb') as f:
    for i in range(65536):
        f.write(struct.pack('P', i))

with open('binary_file.bin', 'rb') as f:
    buf = f.read()
    result = [struct.unpack('P', buf[i:i+8])[0] for i in range(0, 65536*
