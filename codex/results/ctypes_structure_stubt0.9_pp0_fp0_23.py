import ctypes

class S(ctypes.Structure):
    x = ctypes.c_void_p

s = S()

b = b""

s.x = ctypes.addressof(b)

print(s.x)
print(ctypes.string_at(s.x, 0))
</code>
The output is:
<code>51945344
b''
</code>
When I change the last line to <code>print(ctypes.string_at(s.x, 1))</code>, it gives <code>b'\x00'</code>. Actually, even with any negative number as the length, I get the same result <code>b''</code>. Why is this? What could be the reason that the type of a <code>bytes</code> (or <code>str</code>) object is not just a pointer to the data/contents but and additional number?


A:

With <code>string_at</code> you can only access readable memory, that's why <code>-1</code> is the same as 0.
The problem is not the bytes object per se, but <code>string_at</
