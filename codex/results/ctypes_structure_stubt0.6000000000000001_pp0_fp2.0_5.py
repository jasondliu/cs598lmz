import ctypes

class S(ctypes.Structure):
    x = ctypes.c_char
    y = ctypes.c_char

s = S()
s.x = 'a'
s.y = 'b'

print(s.x)
print(s.y)
</code>
Output:
<code>a
b
</code>

