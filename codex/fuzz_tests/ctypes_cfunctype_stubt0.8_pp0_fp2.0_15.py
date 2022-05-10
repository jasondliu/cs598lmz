import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return Py_RETURN_TRUE

@FUNTYPE
def fun2():
    return Py_None

class A:
    def __call__(self):
        return None
    def __len__(self):
        return 2

a = A()
fun()()
fun2()()

if False:
    1
    print("ok")
else:
    pass
fun3 = fun

fun3()()

long(1)

float(1)

complex("0")

complex(1)

a()
