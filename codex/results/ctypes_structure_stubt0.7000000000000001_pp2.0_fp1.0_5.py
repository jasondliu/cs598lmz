import ctypes

class S(ctypes.Structure):
    x = ctypes.c_uint

s = S()
s.x = 0x4040404040404040
print(ctypes.addressof(s.x))

# This shows the output as '4' on 32-bit, and '8' on 64-bit
print(ctypes.sizeof(ctypes.c_ulonglong))

# This shows the output as '4' on 32-bit, and '8' on 64-bit
print(ctypes.sizeof(ctypes.c_uint))

# This shows the output as '4' on 32-bit, and '8' on 64-bit
print(ctypes.sizeof(s.x))
</code>


A:

I ran into this issue as well and only found a solution after stumbling across a post by Hans Passant that said:
"Structures are always aligned on their natural boundaries, which on x64 is 8 bytes. The compiler will automatically insert padding to ensure that."
After some further research, I found that when using ctypes, you can set the alignment by using the _pack_ attribute:
<code>
