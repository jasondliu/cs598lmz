from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>H')
s.unpack(b'\x00\x01')

# 使用Struct类创建一个格式化字符串，并将其用于字节序列
s = Struct('>I')
s.pack(10240099)

# 将文件中的二进制数据读取到一个字节字符串中，然后再将其解压为原始的数据
with open('myfile.zip', 'rb') as f:
    data = f.read()

start = 0
for i in range(3):                      # show the first 3 file headers
    start += 14
    fields = unpack('<IIIHH', data[start:start+16])
    crc32, comp_size, uncomp_size, filenamesize
