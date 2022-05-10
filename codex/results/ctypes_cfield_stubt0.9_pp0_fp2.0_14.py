import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class CObject(object):
    __slots__ = '_cptr',
    _cptr = None

    def __init__(self, ptr=None, flags=ctypes.RTLD_GLOBAL):
        if ptr is None:
            assert hasattr(self, '_cstruct_') and hasattr(self, '_ctor_')
            if _cfuncs is None:
                GetModuleHandle = ctypes.windll.kernel32.GetModuleHandleA
                FindResource = ctypes.windll.kernel32.FindResourceA
                LoadResource = ctypes.windll.kernel32.LoadResource
                LockResource = ctypes.windll.kernel32.LockResource
                SizeofResource = ctypes.windll.kernel32.SizeofResource
                #GetProcAddress = ctypes.windll.kernel32.GetProcAddress
                dll = GetModuleHandle(None)
                #print [name for name in dir(ctypes.windll) if name not in ('windll', '__loader__', '__module__')]
                #ctypes.wind
