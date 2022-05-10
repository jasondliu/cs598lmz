import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return [i for i in range(5)]

def fun2():
    return [i for i in range(5)]

@FUNTYPE
def fun3():
    return [i for i in range(5)]

def fun4():
    return [i for i in range(5)]

@FUNTYPE
def fun5():
    return [i for i in range(5)]

def fun6():
    return [i for i in range(5)]

fun()
fun2()
fun3()
fun4()
fun5()
fun6()

print(fun())
print(fun2())
print(fun3())
print(fun4())
print(fun5())
print(fun6())
