import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

s = S(x=5, y=6)
p = ctypes.pointer(s)

print s.x
print s.y
print p.contents.x
print p.contents.y
print '(%s, %s)' % (p.contents.x, p.contents.y)
</code>
Output:
<code>$ python p.py 
5
6
5
6
(5, 6)
</code>

