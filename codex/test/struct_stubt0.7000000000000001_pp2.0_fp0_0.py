from _struct import Struct
s = Struct.__new__(Struct)
s.format = "H"
s.size = 2
data = bytearray(struct.pack("HH",2,3))
for i in range(3,10):
  data.extend(struct.pack("HH",i,i+1))
d = memoryview(data)
for j in range(5):
  print(j,s.unpack_from(d,2*j))
for j in range(5):
  print(j,s.unpack_from(d,2*(j+5)))
