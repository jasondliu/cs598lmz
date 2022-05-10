from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'B'
s.size = 1
s
s.pack(2)
s.pack(2)
s.unpack(b'\x02')
s.unpack(b'\x02')

#%%
from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'I'
s.size = 4
s
s.pack(2)
s.unpack(b'\x02\x00\x00\x00')
s.unpack(b'\x02\x00\x00\x00')

#%%
s.format = 'II'
s
s.size = 2 * 4
s
s.pack(2, 2)
s.unpack(b'\x02\x00\x00\x00\x02\x00\x00\x00')
s.unpack(b'\x02\x00\x00\x00\x02\x00\x00\x00')

#%%
from collections import namedtuple
Book = namedt
