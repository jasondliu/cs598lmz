import ctypes

class S(ctypes.Structure):
    x = ctypes.c_void_p()
    y = ctypes.c_void_p()

s = S()
print(s.x)
print(s.y)
print(s)
</code>
Output:
<code>0
0
&lt;__main__.S object at 0x10e67e108&gt;
</code>
If you want to see the memory address of <code>s</code>, you can print <code>id(s)</code>.

