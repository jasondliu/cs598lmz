import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    print(33)
    return 33

fun()

# for i in range(10):
#     print(i)
#     if i == 5:
#         print(fun())
