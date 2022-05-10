import ctypes

class S(ctypes.Structure):
    x = ctypes.c_longlong
    y = ctypes.c_longlong

s = S()
s.x = 0x12345678
s.y = 0x90abcdef

f = open("foo.dat", "wb")
f.write(s)
f.close()

f = open("foo.dat", "rb")
s = f.read(16)

s = S.from_buffer_copy(s)

print(s.x)
print(s.y)
</code>

