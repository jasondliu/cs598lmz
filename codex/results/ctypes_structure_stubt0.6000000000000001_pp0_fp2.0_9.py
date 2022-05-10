import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int()
    y = ctypes.c_int()

s = S()
print s.x

s.x = ctypes.c_int(1)
print s.x

s.x.value = 2
print s.x

print type(s.x)
print type(s.x.value)
</code>
Output:
<code>0
1
2
&lt;class 'ctypes.c_int'&gt;
&lt;type 'int'&gt;
</code>

