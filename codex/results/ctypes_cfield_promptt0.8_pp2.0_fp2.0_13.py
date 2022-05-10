import ctypes
# Test ctypes.CField with a struct having a struct field
libc = CDLL(ctypes.util.find_library("c"))
class struct_utmpx(ctypes.Structure):
    pass
struct_utmpx._fields_ = [
    ('ut_type', ctypes.c_short),
    ('ut_tv', ctypes.c_long * 2),
    ('ut_pid', ctypes.c_int32),
    ('ut_id', ctypes.c_char * 4),
    ('ut_user', ctypes.c_char * 32),
    ('ut_line', ctypes.c_char * 32),
    ('ut_host', ctypes.c_char * 256),
    ('exit', struct_utmpx),
    ('ut_session', ctypes.c_long),
    ('pad', ctypes.c_int32 * 2),
    ('ut_addr_v6', ctypes.c_int32 * 16),
    ('unused', ctypes.c_char * 20),
]

libc.getutxent.restype = ctypes.PO
