from _struct import Struct
s = Struct.__new__(Struct)
fmt = '<3s3sHH'

with open('Filter.bmp', 'rb') as input:
   data = input.read(30)
   s.pack_into(data, 0, 'BM', b'\x00\x00', 124, 0)
   print(s.unpack_from(data, 0))
