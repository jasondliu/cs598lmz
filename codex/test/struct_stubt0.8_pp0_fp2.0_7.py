from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('3s3sHH')
print(s)
bin = s.pack('aaa', 'a', 'b', 1, 2)
print(bin)
print(s.unpack(bin))
