import ctypes
# Test ctypes.CFUNCTYPE
class APPP_FUNC(ctypes.Structure):
    _fields_ = [
        ("argc", ctypes.c_int),
        ("argv", ctypes.POINTER(ctypes.c_char_p))
    ]
callable = ctypes.CFUNCTYPE(ctypes.c_int)
app_run = callable()
app_run.argtypes = [ctypes.POINTER(APPP_FUNC)]

def sethook_NDB_init0():
    dl = CDLL("./libndbclient.so")
    dl.NDB_init0.restype = None
    dl.NDB_init0.argtypes = [callable]
    #dl.NDB_init0.term_func = (callable),
    def _callHook(callbackFunc):
        try:
            rc = callbackFunc(ctypes.POINTER(APPP_FUNC)(ctypes.pointer(app_run)))
            print("_callHook (%s)" % str(rc))
        except Exception, err
