import ctypes
# Test ctypes.CField
class CFieldStruct(ctypes.Structure):
    _fields_ = [
        ("a", ctypes.c_int),
        ("b", ctypes.c_long),
        ("c", ctypes.c_double),
        ("d", ctypes.c_char*10),
        ("e", ctypes.c_char*10),
        ("f", ctypes.c_char*10)
    ]
# call a function in a shared library
def GetValue(x):
    dll_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    lib = ctypes.CDLL(os.path.join(dll_dir, "CppDLL.dll"))
    func = lib.multiply
    func.argtypes = [ctypes.c_double]
    func.restype = ctypes.c_double
    return func(x)
# call a function that return a struct
def GetStruct(x):
    dll_dir = os.path.dirname(os.path.dirname
