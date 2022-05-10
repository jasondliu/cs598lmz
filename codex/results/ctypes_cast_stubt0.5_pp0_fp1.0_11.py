import ctypes
ctypes.cast(obj, ctypes.py_object).value

# the same, but using memoryview:
m = memoryview(obj)
# cast to int:
int.from_bytes(m[:4], 'little')
# cast to float:
struct.unpack('&lt;f', m[:4])[0]
# cast to string:
m[:].tobytes().decode()
</code>

