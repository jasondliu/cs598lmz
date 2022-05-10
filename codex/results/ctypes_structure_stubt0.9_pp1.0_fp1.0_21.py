import ctypes

class S(ctypes.Structure):
    x = ctypes.c_float
s = S(8.0)
print(binascii.hexlify(s))
# b'86-40-40-40-40-40-40-40-40-40-40-40-40-40-40-40-40'
print(repr(s))
# S(1)
print(s.x)
</code>
So I think the bytes are being padded with 0s. I tried <code>struct.pack_into(yyyy, s, offset, 8.0,0.0,0.0,0.0)</code>, but no matter what I set offset to <code>repr(s)</code> always starts with S(1).
How can I rewrite this to not pad the structure with 0s so the repr(s) will be correct?

