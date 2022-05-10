import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

class C(ctypes.Structure):
    _fields_ = [('val', S)]

c = C()
c.val = S(1,2)
print(c)
</code>
Output:
<code>&gt;&gt;&gt; python test.py
&lt;__main__.C object at 0x7f1224815150&gt;
</code>

