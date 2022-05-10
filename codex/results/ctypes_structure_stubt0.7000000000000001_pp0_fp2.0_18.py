import ctypes

class S(ctypes.Structure):
    x = ctypes.c_ushort
    y = ctypes.c_ushort
    z = ctypes.c_ushort

val = ctypes.c_ushort(0x1234)
s = S()
s.x = val
s.y = val
s.z = val
</code>
And I expect a result of:
<code>print(s.x.to_bytes(2, "little"))
print(s.y.to_bytes(2, "little"))
print(s.z.to_bytes(2, "little"))
</code>
to be:
<code>b'\x34\x12'
b'\x34\x12'
b'\x34\x12'
</code>
But on Windows it returns:
<code>b'\x12\x34'
b'\x12\x34'
b'\x12\x34'
</code>
So I change the top of the code to:
<code>if sys.byteorder == "little":
    ctypes.c_ushort.
