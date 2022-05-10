import ctypes

class S(ctypes.Structure):
    x = field(ctypes.c_long, offset=8, _bits=7)
    y = field(ctypes.c_long, offset=4, _bits=4)

print(S.x.offset, S.x.size)
print(S.y.offset, S.y.size)
</code>
This outputs (on my machine (python 3.5.2, win32))
<code>(4, 4)
(0, 4)
</code>
Here's why:
<code>pffi.sizeof('l')
</code>
is 4. On win32, its 8 bytes. Oops. It is also 8 on 64 bits architectures. 
So, the <code>offset</code> specified in the code above is doubles.
And, the fact that <code>sizeof('l')</code> is 8 instead of 4 means that the bitfields are swallowed by the following field, ignoring the <code>0</code> padding.
[I doesn't know what to do, other than creating a ticket to get a little helper with bitfield offset and size. Ideally, check ctypes very well
