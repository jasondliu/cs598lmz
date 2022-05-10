import ctypes

class S(ctypes.Structure):
    x = ctypes.c_bool

print 'sizeof(S)', ctypes.sizeof(S)
print 'sizeof(S.x)', ctypes.sizeof(S.x)

s = S()

s.x = True
print s.x

s.x = 0
print s.x

s.x = 1
print s.x

s.x = ''
print s.x

s.x = 'a'
print s.x

s.x = '\x00'
print s.x

s.x = '\x01'
print s.x

s.x = '\x02'
print s.x

# ctypes.c_byte
class S(ctypes.Structure):
    x = ctypes.c_byte

print 'sizeof(S)', ctypes.sizeof(S)
print 'sizeof(S.x)', ctypes.sizeof(S.x)

s = S()

s.x = True
print s.x

s.x = 0

