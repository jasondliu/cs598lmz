import ctypes

class S(ctypes.Structure):
    x = ctypes.c_uint32()
    s = ctypes.c_char_p(b'foo')

x = S()
print(x)
</code>
Output:
<code>$ ./struct_string
&lt;__main__.S object at 0x7f8ec18c3a90&gt;
</code>


A:

<code>ctypes.c_char_p</code> is an object type, not a string type. Use <code>ctypes.c_char</code> to declare a string type:
<code>class S(ctypes.Structure):
    x = ctypes.c_uint32()
    s = ctypes.c_char * 3
</code>

