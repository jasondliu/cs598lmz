import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int,ctypes.c_int,ctypes.c_int)

try:
    print("Trying DLL:", DLL)
    lib = ctypes.cdll.LoadLibrary(DLL)
    lib.TI4X_OpenSerial.argtypes = [ctypes.c_int]
    lib.TI4X_OpenSerial.restype = ctypes.c_int
    lib.TI4X_CloseSerial.argtype = [ctypes.c_int]
    lib.TI4X_CloseSerial.restype = ctypes.c_int
    lib.TI4_SingleTap.argtypes = [ctypes.c_int,ctypes.c_int,ctypes.c_int,ctypes.c_int]
    lib.TI4_SingleTap.restype = ctypes.c_int
    lib.TI4_Move.argtypes = [ctypes.c_int,ctypes.c_int,ctypes.c_int,ctypes.c_int, ctypes.c_int]
    lib.TI4_Move
