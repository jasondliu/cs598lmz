import ctypes
# Test ctypes.CFUNCTYPE
class WIN32_FILE_ATTRIBUTE_DATA(ctypes.Structure):
    pass
WIN32_FILE_ATTRIBUTE_DATA._fields_ = [
    ('dwFileAttributes', ctypes.c_ulong),
    ('ftCreationTime',   ctypes.c_ulong*2),
    ('ftLastAccessTime', ctypes.c_ulong*2),
    ('ftLastWriteTime',  ctypes.c_ulong*2),
    ('nFileSizeHigh',    ctypes.c_ulong),
    ('nFileSizeLow',     ctypes.c_ulong),
]

kernel32 = ctypes.windll.kernel32
GetFileAttributesEx = kernel32.GetFileAttributesExW
call = ctypes.CFUNCTYPE(ctypes.c_bool, ctypes.c_long)( 0, True )
call.errcheck = lambda result, func, args: None
data = WIN32_FILE_ATTRIBUTE_DATA()
GetFileAttributesEx(u'c:\\test.cwb', 0, ctypes.
