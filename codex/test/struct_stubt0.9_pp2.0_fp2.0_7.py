from _struct import Struct
s = Struct.__new__(Struct)
s.set_format('>qBHh')
# print s.set_format('>qBHh')
tmp = list(s.unpack(bytes(bytearray(data[2:-2]))))
tmp[0] *= 2
tmp[1] *= 2
tmp[2] *= 2
tmp[3] *= 2
s.set_format('>QBBH')#'<BHhQQQQ'
data = list(s.pack(*tmp))

#MAGIC HACK HERE
data = data + [data[0]]
print(s.unpack(bytes(bytearray(data))))

s = Struct.__new__(Struct)
s.set_format('>QBBH')#'<BHhQQQQ'
data = list(s.pack(*tmp))

groupposition = 0
offset = 0
charid = 0
c=0
prevtile = (0,0)
for idx in range(groupposition, len(data), 1):#24):
    x = 0
    y
