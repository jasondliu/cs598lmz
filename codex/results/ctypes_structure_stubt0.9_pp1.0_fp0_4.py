import ctypes

class S(ctypes.Structure):
    x = ctypes.c_char * 3
    y = ctypes.c_int * 3

s = S()

s.x[0] = ''
s.x[1] = ''
s.x[2] = ''

s.y[0] = 0
s.y[1] = 0
s.y[2] = 0

print repr(s.x), repr(s.x[0])
print repr(s.y), repr(s.y[0])
</code>
When I run this on 64 bit Linux with Python 2.4.4, I get the following results:
<code>'', '', '' ''
0, 0, 0 0
</code>
Which from the docs I would understand to mean that the memory view of the structure contains the null character. The docs say:
<code>It is safe to assign to a string field ctypes.c_char * 5 as long as the
assigned string is at most five characters long.
</code>
If I instead try to assign to the struct field via the setter property:
<code>s.x = ''
