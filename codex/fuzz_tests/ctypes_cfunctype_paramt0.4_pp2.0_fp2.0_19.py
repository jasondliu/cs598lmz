import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None, ctypes.c_int)
def myfunc(i):
    print("myfunc called with", i)

myfunc_ptr = FUNTYPE(myfunc)
myfunc_ptr(1)

# but this fails:

class MyClass(object):
    def __init__(self, i):
        self.i = i
        self.myfunc_ptr = FUNTYPE(self.myfunc)

    def myfunc(self, i):
        print("myfunc called with", i)

myclass = MyClass(1)
myclass.myfunc_ptr(2)
</code>
The last line fails with:
<code>TypeError: must be convertible to a pointer
</code>
Any ideas?


A:

The problem is that <code>myfunc</code> is an unbound method, and <code>ctypes</code> doesn't know how to convert that to a function pointer. You need to bind the method to an instance first, then pass the bound method to <code>FUNTYPE</code>:
<code>class MyClass(object):
    def
