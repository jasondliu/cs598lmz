import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_void)
class SysKeyInfo(ctypes.Structure):
        _fields_ = [("cbSize", ctypes.c_uint),
                ("dwFlags", ctypes.c_uint),
                ("liTime", ctypes.c_longlong),
                ("hWnd", ctypes.c_void_p),
                ("iVKey", ctypes.c_int),
                ("iRepeat", ctypes.c_int),
                ("iScan", ctypes.c_int),
                ("iExtraInfo", ctypes.c_int),
                ]

CTRL   = 0x0000
SHIFT  = 0x0001
ALT    = 0x0002
EXTEND = 0x0010

dwFlags = {"CTRL": CTRL, "SHIFT": SHIFT, "ALT": ALT, "EXTEND": EXTEND}
vkeys = {"CTRL": 2147483648, "SHIFT": 2147483649, "ALT": 4294967296}

def calc_key(arg):
    if arg[0] in dwFlags.keys
