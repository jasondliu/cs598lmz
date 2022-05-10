from _struct import Struct
s = Struct.__new__(Struct)
s=Struct('i?f') # i = int, ? = boolean, f = float, ensure is the first byte for SerialPacket #
#S=Struct('<i?f') # little endian
print(s.size)
print(s.pack(1,True,2.15))
print(s.unpack(_))

# binary file
#pack to mem/array
a=[1,2,3]
A=array('i',a) # i=int, has "tostring" method
arr = bytearray(A.tostring())
#print(array('i',arr).tolist())
print(struct.unpack('3i', arr[:3*4]))

#unpack from mem/array
b = bytearray(b'0123456789abcdef')
m=memoryview(b)
print(m[0]) # output : 49 (ASCII code of '1')
print(m[:5]) # output : bytearray(b'01234')

#arr = bytearray(A.t
