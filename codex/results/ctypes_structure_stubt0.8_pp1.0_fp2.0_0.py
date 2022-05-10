import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int


s = S()
s.x = 1
s.y = 2

print s._fields_

print 'size:', ctypes.sizeof(s)

print 'value of x:', s.x
print 'value of y:', s.y

print 'address of x:', id(s.x)
print 'address of y:', id(s.y)
</code>
Output:
<code>(('x', &lt;type 'c_int'&gt;), ('y', &lt;type 'c_int'&gt;))
size: 8
value of x: 1
value of y: 2
address of x: 140379810836040
address of y: 140379810836048
</code>
The output is the same on Python 2 and Python 3.

