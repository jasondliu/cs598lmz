import ctypes

class S(ctypes.Structure):
    x = ctypes.c_uint32()
    y = ctypes.c_uint16()
    z = ctypes.c_uint8()
    w = ctypes.c_byte()

ob = S()

print(ob.x, ob.y, ob.z, ob.w)
</code>
output (as in my platform):
<code>0 0 0 0
</code>


A:

It seems that, the Python <code>ctypes</code> module doesn't follow the C packing rule. According to the C standard:
(C2018 7.19 Common definitions <code>&lt;stddef.h&gt;</code> 4, TC3)
<blockquote>
<p>3 Each integer type has an integer conversion rank defined as follows:</p>
<p>— No two signed integer types shall have the same rank, even if they have the same representation,</p>
<p>— The rank of a signed integer type shall be greater than the rank of any signed integer type with less integer conversion rank and greater than the rank of any standard integer type with less integer conversion rank.</
