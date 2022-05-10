import ctypes

class S(ctypes.Structure):
    x = ctypes.c_char_p
    y = ctypes.c_char_p

s = S()
s.x = 'abc'
s.y = 'def'

print s.x, s.y

print s.x.value, s.y.value

print s.x.value is s.y.value

print s.x.value is s.x.value

print s.x.value is s.x

print s.x.value is s.y

print s.x is s.y

print s.x is s.x

print s.x is s.y.value

print s.x.value == s.y.value

print s.x.value == s.x.value

print s.x.value == s.x

print s.x.value == s.y

print s.x == s.y

print s.x == s.x

print s.x == s.y.value
</code>
Output:
<code>abc def
abc def
False
True

