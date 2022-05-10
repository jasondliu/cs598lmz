import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def register_callback(func):
    global _callback
    _callback = FUNTYPE(func)
    _lib.register_callback(_callback)

@register_callback
def my_callback(a, b):
    print("callback got", a, b)
    return a + b

_lib.call_callback(1, 2)
</code>
This works fine, but I don't like the fact that I have to call <code>register_callback</code> to register my callback. Is there a way to make this automatic? I have tried overloading the <code>__init__</code> method, but it does not work.
<code>class MyClass:
    def __init__(self, func):
        global _callback
        _callback = FUNTYPE(func)
        _lib.register_callback(_callback)

    def my_callback(self, a, b):
        print("callback got", a, b)
        return a + b

class MyClass(MyClass):
   
