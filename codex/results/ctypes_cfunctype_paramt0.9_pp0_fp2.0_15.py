import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double)

def Load():
    print("Loading DLL and mapping functions...")
    dll_path = "./EQLib.dll"
    dlib = ctypes.CDLL(dll_path)
    dlib.EMDMap.argtypes = [ctypes.c_double, ctypes.c_int, ctypes.c_int, FUNTYPE]
    dlib.BumpsMap.argtypes = [ctypes.c_double, ctypes.c_int, ctypes.c_int, FUNTYPE]

    print("Testing emd...")
    emd = dlib.EMDMap(8, 20, 30, FUNTYPE(emd_loop))
    emd_data = emd.read()
    print("emd_data", emd_data)

    print("Testing bumps...")
    bumps = dlib.BumpsMap(9, 50, 40, FUNTYPE(bumps_loop))
    bumps_data = bumps.read()
    print("bumps_data", bumps_data)
    bumps_data = bumps.read()
