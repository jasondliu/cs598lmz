from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>I')
s.size

# 或者从类中创建实例
from _struct import Struct
Struct('>I')

# 从类创建实例的方式更加常用
from _struct import Struct

with open('myfile.zip', 'rb') as f:
    data = f.read()

start = 0
for i in range(3):                      # show the first 3 file headers
    start += 14
    fields = Struct('>IHH').unpack_from(data, start)
    crc32, comp_size, uncomp_size = fields

    print(f'{i}: crc32={hex(crc32)}, comp_size={comp_size}, uncomp_size={uncomp_size}')

