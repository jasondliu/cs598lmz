import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42

x = fun

print x.fname
print x(1)
'fun()'
42
</code>
So,
instead of declaring a function like that:
<code>def plus(a,b):
    return a + b
</code>
why not this one?
<code>@FUNTYPE       
def plus(a,b):
    return a + b
</code>
you have the same result. Plus, if you want to call the function from the C code then you have the handle to it. In other words, the function declaration is a <code>def</code> statement and nothing else, it does not have anything to do with function types (there are none in Python anyway), <code>@FUNTYPE</code> simply decorates the function with a CFUNCTYPE instance.

