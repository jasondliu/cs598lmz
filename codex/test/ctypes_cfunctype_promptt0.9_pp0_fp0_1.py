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

