import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "Hello World"
fun()

#class myclass(object):
#    def __init__(self, a):
#        self.a = a
#    def __call__(self, *args, **kwargs):
#        return self.a
#f = myclass("Hello World")
#f()

class myclass(object):
    def __init__(self, a):
        self.a = a
    def __call__(self, *args, **kwargs):
        return self.a
f = myclass("Hello World")
fun = ctypes.CFUNCTYPE(ctypes.py_object)(f)
fun()
</code>
When I call <code>fun()</code> with <code>@FUNTYPE</code> it prints <code>Hello World</code> as expected. However, when I call <code>fun()</code> with <code>fun = ctypes.CFUNCTYPE(ctypes.py_object)(f)</code>, I get the error:
<code>Traceback (most recent call last):
 
