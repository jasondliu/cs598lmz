import ctypes

class S(ctypes.Structure):
    x = ctypes.c_uint32
    y = ctypes.c_uint32

s = S()
s.x = 0x11111111
s.y = 0x22222222

serialized = b'\x11\x11\x11\x11\x22\x22\x22\x22'
buf = ctypes.c_buffer(serialized)

newS_from_str = S.from_buffer(buf)
newS_from_bytearray = S.from_buffer(bytearray(serialized))

print(newS_from_str.x, newS_from_str.y)
print(newS_from_bytearray.x, newS_from_bytearray.y)

# 327763445 16909060
# 327763445 16909060
</code>
This allows you to do something like:
<code>with open("somefile", "rb") as fin:
    serialized = fin.read()

buf = ctypes.c_buffer(serialized)
records =
