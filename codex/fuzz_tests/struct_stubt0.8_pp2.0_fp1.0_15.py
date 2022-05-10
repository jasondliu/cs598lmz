from _struct import Struct
s = Struct.__new__(Struct)

s

#%%
s.__unpack__(b'\x12\x34\x56')

#%%
s.format = '>i'
s.size = s.__calcsize__()
s.unpack(b'\x12\x34\x56')

#%%
s = Struct(format = '>i')
s.size
s.unpack(b'\x12\x34\x56')

#%%
s = Struct()
s.format = '>i'
s.size
s.unpack(b'\x12\x34\x56')

#%%
s = Struct()
s.__init__('>i')
s.format
s.size
s.pack(12345678)
s.unpack(b'\x12\x34\x56')

#%%
s = Struct(format = '>i')
s.format
s.size
s.pack(12345678)
s.unpack(b'\x12\x34\x56')

#
