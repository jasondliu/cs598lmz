from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i?f')
s.size

s.pack(1, False, 3.14)

s.unpack(_)

s.unpack_from(bytes, 4)

import array
nums = array.array('i', [1, 2, 3, 4])
s.pack_into(nums, 0, 1, False, 3.14)
nums

s.unpack_from(nums, 1)

#%%
# 使用编码和解码
data = b'\x00\x124V\x00x\x90\xab\x00\xcd\xef\x01\x00#\x004'
len(data)

int.from_bytes(data, 'little')

(int.from_bytes(data, 'big'))

x = 94522842520747284487117727783387188
x.to_bytes(16, 'big')

