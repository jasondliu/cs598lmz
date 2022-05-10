import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

class MyObj:
    def __init__(self, x):
        self.x = x

    def hello(self, y):
        print("Hello", self.x, y)

def foo(x):
    print("foo", x)

def bar(y):
    print("bar", y)

# ctypes.cast(obj, ctypes.py_object)
# ctypes.cast(obj, ctypes.c_void_p)
# ctypes.pythonapi.PyCapsule_GetPointer(...)

# https://stackoverflow.com/questions/47891940/python-ctypes-calling-a-c-function-with-a-callback
def call_with_callback(callback_func, arg):
    c_callback_func = FUNTYPE(callback_func)
    return c_callback_func(arg)

myobj = MyObj("world")

call_with_callback(myobj.hello, 17)
call_with_callback(foo, 3)
