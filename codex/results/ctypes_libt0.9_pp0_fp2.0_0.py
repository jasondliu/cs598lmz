import ctypes
ctypes.stdcall_abi = ctypes.CDLL.__getattr__

log = logging.getLogger()

class TOX_CONNECTION:
    NONE = ctypes.c_int(0)
    TCP = ctypes.c_int(1)
    UDP = ctypes.c_int(2)

class TOX_CONNECTION_P(ctypes.c_void_p):
    pass
TOX_CONNECTION_P_P = ctypes.POINTER(TOX_CONNECTION_P)

class TOX_USER_STATUS:
    NONE = ctypes.c_int(0)
    AWAY = ctypes.c_int(1)
    BUSY = ctypes.c_int(2)

class TOX_USER_STATUS_P(ctypes.c_void_p):
    pass
TOX_USER_STATUS_P_P = ctypes.POINTER(TOX_USER_STATUS_P)

class TOX_FILE_CONTROL:
    RESUME = ctypes.c_
