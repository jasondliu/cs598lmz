import ctypes
ctypes.pythonapi.PyFile_AsFile.restype = ctypes.POINTER(FILE)
ctypes.pythonapi.PyFile_AsFile.argtypes = [PyObject]
file_global = None

def stdin_getchar():
    global file_global
    if file_global is None:
        file_global = ctypes.pythonapi.PyFile_AsFile(sys.stdin)
    return _getchar_unlocked(file_global)

def getchar():
    global file_global
    if file_global is None:
        file_global = ctypes.pythonapi.PyFile_AsFile(sys.stdin)
    return _getchar_unlocked(file_global)

def input(): return sys.stdin.readline().rstrip()

# endregion

def list2d(a, b, c): return [[c] * b for i in range(a)]
def list3d(a, b, c, d): return [[[d] * c for j in range(b)] for i in range(a)]
def list4d(a
