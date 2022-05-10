import _struct

_debug = False


# Some data types.
DWORD = c_ulong
WORD = c_ushort

# "structs"
class BYTE(Structure):
    _fields_ = [('a', c_ubyte)]

class USHORT(Structure):
    _fields_ = [('a', c_ushort)]

class LPSTR(Structure):
    _fields_ = [('a', c_char_p)]

class HANDLE(Structure):
    _fields_ = [('a', c_void_p)]

class SYSTEMTIME(Structure):
    _fields_ = [
        ('wYear', WORD),
        ('wMonth', WORD),
        ('wDayOfWeek', WORD),
        ('wDay', WORD),
        ('wHour', WORD),
        ('wMinute', WORD),
        ('wSecond', WORD),
        ('wMilliseconds', WORD),
    ]
