import ctypes

class S(ctypes.Structure):
    x = ctypes.c_double
    y = ctypes.c_double

buffer = S(0,0)

w = ctypes.windll.kernel32.VirtualAlloc(
    ctypes.c_int(-1),
    ctypes.sizeof(ctypes.c_int),
    ctypes.c_int(0x2000),
    ctypes.c_int(0x04)
)

ctypes.windll.kernel32.WriteProcessMemory(
    ctypes.c_int(0xffffffff),
    w,
    ctypes.byref(buffer),
    ctypes.sizeof(ctypes.c_int),
    ctypes.byref(ctypes.c_int(0))
)

print w

x = ctypes.windll.user32.FindWindowA(
    ctypes.c_char_p(b'Notepad'),
    ctypes.c_char_p(b'Untitled - Notepad')
)

ctypes.windll.user32.SendMessageA(x, ctypes.c_int(
