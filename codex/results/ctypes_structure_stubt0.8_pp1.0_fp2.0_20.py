import ctypes

class S(ctypes.Structure):
    x = ctypes.c_uint8
    y = ctypes.c_uint16

ptr = ctypes.cast(ctypes.c_uint32(16), ctypes.POINTER(S))
print repr(ptr[0])

ptr = ctypes.cast(ctypes.c_uint32(20), ctypes.POINTER(S))
print repr(ptr[0])

ptr = ctypes.cast(ctypes.c_uint32(24), ctypes.POINTER(S))
print repr(ptr[0])

ptr = ctypes.cast(ctypes.c_uint32(28), ctypes.POINTER(S))
print repr(ptr[0])
</code>
Result:
<code>&lt;__main__.S instance at 0x02E74718&gt;
&lt;__main__.S instance at 0x02E74748&gt;
&lt;__main__.S instance at 0x02E74778&gt;
&lt;__main__.S instance at 0x02E747A8&gt;
</code>
The
