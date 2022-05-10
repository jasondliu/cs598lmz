import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None)

# Fetch a function from a DLL.
mkinfo = ctypes.cdll.LoadLibrary('build/mkinfo.dll').mkinfo
mkinfo.restype = FUNTYPE

# Show it works.
mkinfo()
