import ctypes

class S(ctypes.Structure):
    x = ctypes.c_char_p()
s = S()
print repr(s)

s.x = "ABC"
print repr(s)
</code>
prints:
<code>&lt;__main__.S object at 0x0000000002A1F3D0&gt;
&lt;__main__.S object at 0x0000000002A1F3D0&gt;
</code>

