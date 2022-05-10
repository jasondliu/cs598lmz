import ctypes
# Test ctypes.CFUNCTYPE()
# CFUNCTYPE(restype, *argtypes, use_errno=False, use_last_error=False)

# o = ctypes.CFUNCTYPE()

# Test for SetEvent()
HANDLE = ctypes.c_ulong
WinError = ctypes.WinError

class EVENT_T(ctypes.Structure):
    _fields_ = [("overlapped", OVERLAPPED)]

SetEvent = ctypes.windll.kernel32.SetEvent
SetEvent.argtypes = [HANDLE]
SetEvent.restype = ctypes.c_int

h = HANDLE()
h.value = 0xffffffffB0015E0

print("This is h:  ", h)

try:
    SetEvent(h)
    print("SetEvent() Success!")
except WinError as e:
    print("SetEvent() failed:  %s" % e)

# Test ctypes.c_char_p()

a = ctypes.c_char_p()
print("This is a
