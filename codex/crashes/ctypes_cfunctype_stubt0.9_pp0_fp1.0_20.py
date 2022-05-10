import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    print("value of bug is :{}".format(bug))
if __name__ == '__main__':
    cmp_callback = fun
    cmp_callback()
