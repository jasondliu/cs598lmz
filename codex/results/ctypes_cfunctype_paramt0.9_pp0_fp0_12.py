import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.POINTER(ctypes.c_double),
                           ctypes.c_void_p)

MagABS = FUNTYPE(('MagnetAbs', DllMagnet))
MagABS.restype = ctypes.c_double
MagABS.argtypes = [ctypes.POINTER(ctypes.c_double),
                   ctypes.c_void_p]

MagABSError = FUNTYPE(('MagnetAbsError', DllMagnet))
MagABSError.restype = ctypes.c_double
MagABSError.argtypes = [ctypes.POINTER(ctypes.c_double),
                        ctypes.c_void_p]

def magnet_abs(pos_tel, config):
    """
    This function calculates the absorption of a selected magnet
    in the telescope.
    
    Parameters
    ----------
    pos_tel : array
        Position of the center of the telescope.
    config : dictionary
        Contains the data needed to calculate the absorption of a
        magnet in a telescope.

    Returns

