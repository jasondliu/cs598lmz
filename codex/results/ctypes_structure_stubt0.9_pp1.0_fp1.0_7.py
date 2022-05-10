import ctypes

class S(ctypes.Structure):
    x = ctypes.string_at(1, 4)

s = S()
print s.x
s.x = 'ab'
print s.x
s.x = 'abc'
print s.x
s.x = 'abcd'
print s.x
s.x = 'abcde'
print s.x
