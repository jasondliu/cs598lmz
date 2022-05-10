import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int()
    y = ctypes.c_int()

s = S()
print s
print s.x
print s.y

s.x = 1
s.y = 2
print s
print s.x
print s.y
</code>
output:
<code>&lt;__main__.S instance at 0x7f4b4c8e2f80&gt;
0
0
&lt;__main__.S instance at 0x7f4b4c8e2f80&gt;
1
2
</code>

