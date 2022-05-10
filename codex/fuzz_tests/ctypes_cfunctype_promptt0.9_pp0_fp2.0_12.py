import ctypes
# Test ctypes.CFUNCTYPE, issue #13230

if os.name == "nt" and sys.version_info[0:2] >= (3,4):
    import _ctypes
    def callback(a, b, c):
        return 0
    done = False
    for dll_name in ['msvcr100', 'msvcrt']:
        try:
            dll = ctypes.cdll.__getattribute__(dll_name)
        except:
            continue
        try:
            qsort = getattr(dll, 'qsort')
        except:
            continue
        if qsort.argtypes is None:
            continue
        qsort.argtypes = [_ctypes.Py_UNSIGNEDCHAR_p,
                          ctypes.c_ulong,
                          ctypes.c_ulong,
                          ctypes.CFUNCTYPE(ctypes.c_int,
                                           ctypes.c_int,
                                           ctypes.c_int)]
        qsort.restype = None
        done = True
        break
    if sys
