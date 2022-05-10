import ctypes

class S(ctypes.Structure):
    x = ctypes.c_char
    y = ctypes.c_char

class D(ctypes.Structure):
    x = ctypes.c_char
    y = ctypes.c_char
    z = ctypes.c_char

print(ctypes.sizeof(S))
print(ctypes.sizeof(D))
</code>
This outputs:
<code>2
3
</code>
However, when I look at the source of the ctypes module, I see:
<code>self._fields_ = []
self._pack_ = 1
</code>
Which I expect should pack the Structures as tightly as possible (i.e. as closely as it can to the way it would be packed in C).
When I add <code>__slots__</code> to the Structures, I get the correct sizes (1 and 2 respectively), but I'd like to avoid this if possible, since the extra Structures I'm working with will have a lot of fields.
Why is this happening? Is this the expected behaviour? Is there a way to pack them tightly without using <code>__slots
