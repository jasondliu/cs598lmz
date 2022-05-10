import ctypes
# Test ctypes.CFieldTypes.
if not getattr(ctypes, 'CFieldTypes', 0):
    print('===SKIP===')
    raise SystemExit

print(ctypes.sizeof(ctypes.INT64))
print(ctypes.sizeof(ctypes.STRING_ATOM))
print(ctypes.sizeof(ctypes.S1.S1a))
print(ctypes.sizeof(ctypes.S1.S1b))
print(ctypes.sizeof(ctypes.S2.S2a))
print(ctypes.sizeof(ctypes.S2.S2b))
print(ctypes.sizeof(ctypes.S2.S2x))
