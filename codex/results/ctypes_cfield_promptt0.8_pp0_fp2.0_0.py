import ctypes
# Test ctypes.CField.
try:
    ctypes.CField
except AttributeError:
    print("SKIP")
    raise SystemExit

# Allocate a buffer for a struct
buf = ctypes.create_string_buffer(4)

f = ctypes.CField(0, 1, ctypes.c_int16)
f.set(buf, 1)
print(buf[:])
print(hex(f.get(buf)))

f = ctypes.CField(0, 1, ctypes.c_uint16)
f.set(buf, 1)
print(buf[:])
print(hex(f.get(buf)))

f = ctypes.CField(1, 1, ctypes.c_int16)
f.set(buf, 1)
print(buf[:])
print(hex(f.get(buf)))

f = ctypes.CField(1, 1, ctypes.c_uint16)
f.set(buf, 1)
print(buf[:])
print(hex(f.get(buf)))

f = ctypes.
