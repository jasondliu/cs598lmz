import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return []

def main():
    fun()

if __name__ == "__main__":
    main()
