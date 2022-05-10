import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = 16 * "ab"
    z = 16 * "cd"
    w = 16 * "ef"

strct = S()

strct.x = 123
strct.y = "hello"

buf = ctypes.create_string_buffer(16)
buf.value = "world"
ctypes.memmove(ctypes.addressof(strct) + strct.y.offset, ctypes.addressof(buf), 16)

print(ctypes.string_at(ctypes.addressof(strct) + strct.y.offset, 12))
print(ctypes.string_at(ctypes.addressof(strct) + strct.z.offset, 16))
print(ctypes.string_at(ctypes.addressof(strct) + strct.w.offset, 16))
