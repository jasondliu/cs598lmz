import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None,ctypes.c_float,ctypes.c_float)
class FooMe(method):
    def __init__(self,fptr):
        self.fptr = FUNTYPE(fptr)
    def __call__(self,*args,**kwargs):
        print(self)
        self.fptr(ctypes.c_float(1.0),ctypes.c_float(2.0))
        return method.__call__(self,*args,**kwargs)
foo = FooMe(my_c_function)
class A(object):
    @foo
    def bar(self):
        pass
A().bar()
</code>
This means that when you add the decorator, you don't have the function's arguments, but you do have the <code>self</code> of the class, so you can access its attributes.
I'm not sure you can access the original function's attributes, but if you can't, you can try inheriting from <code>method</code> instead of from <code>object</code>.

