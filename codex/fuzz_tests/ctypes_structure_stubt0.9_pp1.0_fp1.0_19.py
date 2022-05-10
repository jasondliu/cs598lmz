import ctypes

class S(ctypes.Structure):
    x = ctypes.c_short
    y = ctypes.c_ushort
    z = ctypes.c_long
</code>
Results in:
<code>S.x 
=&gt; c_short(0) 
S.y 
=&gt; c_ushort(0) 
S.z 
=&gt; c_long(0) 
</code>
Odd, isn't it?
From Ctypes text:
<blockquote>
<p>The automatic initialization from 0 isn’t always convenient. </p>
</blockquote>
But for me, it's always inconvenient. Is there a way to turn this off?


A:

Simplified, it looks like it is initialized when it is first read.  When you first read <code>z</code>, <code>y</code> is read, which initializes <code>x</code>.
<code>class S(ctypes.Structure):
    x = ctypes.c_short
    y = ctypes.c_ushort
    z = ctypes.c_long

