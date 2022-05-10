from _struct import Struct
s = Struct.__new__(Struct)
s.initialize() # make a new instance of the Struct class
#print(s)
zero = s.pack(2, 100000)
print(len(zero))
##
##
##text = 'Hello world'
##struct.pack('i',len(text))
##print(struct.pack('i', len(text)))
##
##
##### Sending data using multiple packets
##import struct
##format = 'I 2s f'
##s = struct.Struct(format)
##print(s.size)
##
##packed_data = s.pack(123, b'hi', 3.1415926)
##print(packed_data)
##
##unpacked_data = s.unpack(packed_data)
##print(unpacked_data)
