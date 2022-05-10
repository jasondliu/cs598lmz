import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

s = S()
s.x = 1
s.y = 2

print s.x, s.y

# s.x = 'a'
# print s.x, s.y

# s.x = 1
# s.y = 'a'
# print s.x, s.y

# s.x = 'a'
# s.y = 'b'
# print s.x, s.y

# s.x = 'a'
# s.y = 2
# print s.x, s.y

# s.x = 1
# s.y = 'b'
# print s.x, s.y
