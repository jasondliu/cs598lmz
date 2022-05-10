import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
def py_print(arg):
    print(arg)
    return arg + 1

def main():
    py_print(5) # Should print 5
    c_print = FUNTYPE(py_print)
    c_print(5) # Should print 5

if __name__ == "__main__":
    main()
