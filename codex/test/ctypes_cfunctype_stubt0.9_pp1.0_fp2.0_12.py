import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 'Hello World!'

CFUNCTYPE = ctypes.CFUNCTYPE
def build_fun(cfun):
    return CFUNCTYPE(ctypes.py_object)(cfun)

if __name__ == '__main__':
    cfun = CFUNCTYPE(ctypes.py_object)(fun)
    print(type(cfun), type(fun), type(build_fun(fun)))
    print(cfun(), fun(), build_fun(fun)())
