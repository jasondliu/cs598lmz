import ctypes

class S(ctypes.Structure):
    x = ctypes.c_uint16
    y = ctypes.c_uint16

s = S()
s.x = 0x12345678
s.y = 0xabcdef12

print 's.x = 0x%x, s.y = 0x%x' % (s.x, s.y)

buff = ctypes.create_string_buffer(ctypes.sizeof(S))
ctypes.memmove(buff, ctypes.addressof(s), ctypes.sizeof(S))

new_s = ctypes.cast(buff, ctypes.POINTER(S)).contents
print 'new_s.x = 0x%x, new_s.y = 0x%x' % (new_s.x, new_s.y)
