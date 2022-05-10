import ctypes

class S(ctypes.Structure):
    x = ctypes.c_char_p
    y = ctypes.c_char_p
    z = ctypes.c_char_p

s = S()
s.x = 'a'
s.y = 'b'
s.z = 'c'

print s.x
print s.y
print s.z

s.x = 'x'
s.y = 'y'
s.z = 'z'

print s.x
print s.y
print s.z

s.x = '1'
s.y = '2'
s.z = '3'

print s.x
print s.y
print s.z
</code>
The output is:
<code>a
b
c
x
y
z
1
2
3
</code>

