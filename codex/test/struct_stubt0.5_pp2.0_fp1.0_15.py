from _struct import Struct
s = Struct.__new__(Struct)
print(s)

#import _struct
#print(_struct.Struct.__new__(_struct.Struct))

#import struct
#print(struct.Struct.__new__(struct.Struct))

#import _struct
#print(_struct.Struct)

#import struct
#print(struct.Struct)

#import _struct
#print(_struct.Struct.__new__)

#import struct
#print(struct.Struct.__new__)

#import _struct
#print(_struct.Struct.__new__.__code__.co_code)

#import struct
#print(struct.Struct.__new__.__code__.co_code)

#import _struct
#print(_struct.Struct.__new__.__code__.co_code.hex())

#import struct
#print(struct.Struct.__new__.__code__.co_code.hex())
