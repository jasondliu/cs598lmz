import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None)
class _stdcall_callback(FUNTYPE):
    def __init__(self, func, restype=None, argtypes=None, errcheck=None):
        FUNTYPE.__init__(self, restype, argtypes, errcheck)
        self.func = func
    def __call__(self, *args):
        return self.func(*args)
    def __eq__(self, other):
        return other == self.func
    def __ne__(self, other):
        return other != self.func
    def __hash__(self):
        return hash(self.func)

def stdcall_callback(func, restype=None, argtypes=None, errcheck=None):
    return _stdcall_callback(func, restype, argtypes, errcheck)

def dll_function(dll, name, restype, argtypes, errcheck=None):
    func = getattr(dll, name)
    func.argtypes = argtypes
    func.restype = restype
    if errcheck is not None:
        func.errcheck
