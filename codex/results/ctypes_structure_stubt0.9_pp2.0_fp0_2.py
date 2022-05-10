import ctypes

class S(ctypes.Structure):
    x = ctypes.c_ubyte(9)[2]
    y = ctypes.c_wchar(3)[1]
    z = ctypes.c_char(23)[3]

print(S.x)

&gt;&gt;&gt; &lt;class '__main__.S.x'&gt;
</code>
Another question, i think that <code>y</code> and <code>z</code> are of no-use to me, because i cant access the <code>z</code> field of the data structure at a certain index
<code>data.z(1) # gives me a type error, i think it should atleast give me a c_char instance
</code>
I think <code>x</code> is the field i want to use, but its a little unclear, in <code>ctypes arrays</code> are you meant to be able to access elements like <code>a[b]</code> where <code>a</code> is of type <code>c_ubyte*2</code> and <code>b</code>
