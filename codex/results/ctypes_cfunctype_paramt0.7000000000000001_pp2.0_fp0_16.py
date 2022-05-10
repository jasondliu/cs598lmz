import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int)

# Python is not guaranteed to have a long int
# long long is guaranteed to be at least 64-bit
# We use that for storing our tokens
TOKEN_TYPE = ctypes.c_longlong

# The shared library
# The library name on Windows is different
if sys.platform == "win32":
    # On Windows, look for the file in the same directory as the script
    LIBRARY = ctypes.CDLL(os.path.join(os.path.dirname(__file__), "liblex.dll"))
else:
    LIBRARY = ctypes.CDLL("liblex.so")

# The structure used in the C code:
class YY_BUFFER_STATE(ctypes.Structure):
    pass
YY_BUFFER_STATE_P = ctypes.POINTER(YY_BUFFER_STATE)

# The function prototypes
yy_scan_string = LIBRARY.yy_scan_string
yy_scan_string.restype = YY_BUFFER_STATE_P
yy_scan_string.argtypes =
