import ctypes

class S(ctypes.Structure):
    x = ctypes.c_longlong()

_zlib_version = ctypes.CDLL(_zlib.__file__).zlibVersion
if _sys.version_info > (3,):
    buf = ctypes.c_buffer(bytes("", 'ascii'))
else:
    buf = ctypes.c_buffer("")
_zlib_version.restype = ctypes.c_char_p
_zlib_version.argtypes = None,
_zlib_version(buf)
ZLIB_PREFIX = "1.2"
ZLIB_VERSION = _zlib_version().decode().strip()
assert ZLIB_VERSION.startswith(ZLIB_PREFIX)
ZLIB_MINOR_VERSION = ZLIB_VERSION[len(ZLIB_PREFIX):]
ZLIB_MINOR_VERSION = int(ZLIB_MINOR_VERSION)

ERROR_MSG = """
  You have linked against dynamic libzlib. This is a security risk
since these libraries are not versioned.

A versioned version is available at
  https
