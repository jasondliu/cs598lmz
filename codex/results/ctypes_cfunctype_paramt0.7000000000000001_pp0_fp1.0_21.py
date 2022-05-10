import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

class MyObject(ctypes.Structure):
    pass

MyObject_p = ctypes.POINTER(MyObject)

def call(ob, arg1, arg2):
    return arg1 + arg2

mycallback = FUNTYPE(call)

c_func = ctypes.CFUNCTYPE(MyObject_p, MyObject_p)
callback_type = ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.c_int)

lib = ctypes.CDLL("libtest.so")
obj = MyObject()

# obj has no member function_pointer
obj.function_pointer = c_func(ctypes.cast(mycallback, ctypes.c_void_p))
print(obj.function_pointer)

# obj has no member callback
obj.callback = callback_type(mycallback)
print(obj.callback)

result = lib.call(obj)
print(result)
</code>
So there
