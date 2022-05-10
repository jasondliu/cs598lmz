import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int()

class X(object):
    def __init__(self):
        self._i = S()

def main():
    py_x = X()
    cp_x = ctypes.cast(id(py_x), ctypes.POINTER(S))
    # This is not correct, it accesses x attribute of py_x.__class__
    print(cp_x.contents.x)

if __name__ == "__main__":
    main()
