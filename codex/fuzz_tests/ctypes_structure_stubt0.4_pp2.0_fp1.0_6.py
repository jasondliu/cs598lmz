import ctypes

class S(ctypes.Structure):
    x = ctypes.c_char * 2
    y = ctypes.c_char * 2

s = S()
print s.x
print s.y
print s.x is s.y
</code>
Output:
<code>&lt;__main__.c_char_Array_2 object at 0x0000000002A9D828&gt;
&lt;__main__.c_char_Array_2 object at 0x0000000002A9D828&gt;
True
</code>

