import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    print("Hello")
    return "Hello"

cpp.guest_f_del("error")
cpp.guest_fun_map["error"] = fun
cpp.guest_f_del("error")
cpp.guest_fun_map["error"] = fun
cpp.guest_f_del("error")
cpp.guest_f("error")
print("Hello")
```
