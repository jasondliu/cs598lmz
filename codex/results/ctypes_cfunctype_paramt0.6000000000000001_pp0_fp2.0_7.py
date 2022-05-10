import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def set_func(func):
    ctypes.pythonapi.PyThreadState_SetAsyncExc(
        ctypes.c_long(thread.ident), FUNTYPE(func))

def func():
    print("Terminating thread")

set_func(func)
</code>
This works as expected, but I am wondering if there is a way to do this without using <code>ctypes</code>?

