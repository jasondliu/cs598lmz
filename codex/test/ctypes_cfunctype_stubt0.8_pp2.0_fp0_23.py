import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    print("inside fun1")
def fun2():
    print("inside fun2")
i = 0
fun_list = [fun,fun2,fun]
while True:
    print("inside while")
