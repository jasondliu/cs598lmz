import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def make(T, val):
    return ctypes.cast((T * 1)(), ctypes.POINTER(T))[0]

UINT = ctypes.c_uint
INT = ctypes.c_int
BYTE = ctypes.c_byte
WORD = ctypes.c_ushort
ULONG = ctypes.c_ulong
LONG = ctypes.c_long
DWORD = ctypes.c_ulong
PBYTE = ctypes.POINTER(BYTE)
PWORD = ctypes.POINTER(WORD)
PULONG = ctypes.POINTER(ULONG)
PLONG = ctypes.POINTER(LONG)
PDWORD = ctypes.POINTER(DWORD)
LPBOOL = ctypes.POINTER(ctypes.c_bool)
LPDWORD = ctypes.POINTER(DWORD)
LPVOID = ctypes.c_void_p
CHAR = ctypes.c_char
WCHAR = ctypes.c_wchar
LPSTR = ctypes.c_char_p
L
