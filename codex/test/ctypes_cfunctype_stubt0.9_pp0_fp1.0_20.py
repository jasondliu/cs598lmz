import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    temp = 10
    print("value of bug is :{}".format(bug))
    print("value of temp is :{}".format(temp))
    return 0

if __name__ == '__main__':
    cmp_callback = fun
    cmp_callback()
