import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int16(0)
    y = ctypes.c_int16(0)

print(S.__align__)

foo = S()
# foo.x = foo.y = 0x7fff
foo.x = foo.y = 0x8000
print(foo.x)
print(foo.y)

# foo.x = foo.y = 0x8001
foo.x = foo.y = 0x8002
print(foo.x)
print(foo.y)

# foo.x = foo.y = 0xffff
foo.x = foo.y = 0x10000
print(foo.x)
print(foo.y)

bytes = S.x.from_buffer(foo)
bytes = S.y.from_buffer(foo)
print(bytes)
</code>

