import ctypes

class S(ctypes.Structure):
    x = ctypes.c_uint32
    y = ctypes.c_uint32

array = (
    S(0x43, 0x0),
    S(0x0, 0x0),
    S(0x43, 0x0),
    S(0x0, 0x0),
)
buf = ctypes.create_string_buffer(ctypes.sizeof(ctypes.c_uint8) * len(array))
for i, e in enumerate(array):
    struct.pack_into("&gt;II", buf, i * 2 * ctypes.sizeof(ctypes.c_uint32), e.x, e.y)
print(buf.raw)
</code>
Output:
<code>b'C\x00\x00\x00\x00\x00\x00\x00\x00C\x00\x00\x00\x00\x00\x00\x00'
</code>

