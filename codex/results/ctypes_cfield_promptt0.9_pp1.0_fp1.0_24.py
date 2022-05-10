import ctypes
# Test ctypes.CField
# (tested in test_structseq.py)

libc = ctypes.cdll.msvcrt
stdcall = ctypes.WINFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
z = stdcall(("printf", libc))
# This, of course, generates some debug output
args = 'PYnN'.encode('utf-8') + ctypes.create_string_buffer(b'Hello world\n')
rc = z(5, args)
if rc != 14:
    raise ValueError("didn't write all characters")

# No crash -- success
print("done :-)")
