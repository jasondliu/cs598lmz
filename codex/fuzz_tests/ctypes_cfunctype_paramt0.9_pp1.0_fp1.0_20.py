import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int,ctypes.c_int)
dll.add.argtypes = (ctypes.c_int,ctypes.c_int)
dll.add.restype = ctypes.c_int

ADD = FUNTYPE(("add", dll)) #为了将dll对象绑定到函数指针对象上，这里必须是元组

def main():
    r = dll.add(1,2)
    print("r = ",r,"type = ",type(r))

    f = ADD(1, 2)
    print("f = ", f)

if __name__ == "__main__":
    main()
