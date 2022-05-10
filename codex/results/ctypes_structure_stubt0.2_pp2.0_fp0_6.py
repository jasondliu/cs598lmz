import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

s = S()
s.x = 1
s.y = 2

print(s.x, s.y)

s2 = S.from_buffer_copy(s)
s2.x = 3

print(s.x, s.y)
print(s2.x, s2.y)

print(s.raw)
print(s2.raw)

print(s.raw == s2.raw)

print(s.raw_address)
print(s2.raw_address)

print(s.raw_address == s2.raw_address)

print(s.raw_lengths)
print(s2.raw_lengths)

print(s.raw_lengths == s2.raw_lengths)

print(s.raw_itemsize)
print(s2.raw_itemsize)

print(s.raw_itemsize == s2.raw_itemsize)

print(s.raw_ndim)
print(
