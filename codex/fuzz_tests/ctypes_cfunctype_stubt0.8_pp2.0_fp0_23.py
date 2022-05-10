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
    time.sleep(2)
    print("inside sleep")
    fun_list[i]()
    print("count %s"%i)
    i += 1
    print("count after increment %s"%i)
    if i == 3:
        print("inside i == 3")
        i = 0
