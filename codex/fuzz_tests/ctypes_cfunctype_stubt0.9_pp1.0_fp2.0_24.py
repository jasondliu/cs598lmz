import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1

def fun1():
    return 1

def f():
    pass
print fun.__module__
print fun.__code__
print fun.__class__
print (int, ctypes.py_object)[fun.__class__ is ctypes.py_object]

print fun1.__module__
print fun1.__code__
print fun1.__class__
print (int, ctypes.py_object)[fun1.__class__ is ctypes.py_object]

print f.__module__
print f.__code__
print f.__class__
print (int, ctypes.py_object)[f.__class__ is ctypes.py_object]
</code>
I get the following result:

<code>__main__
&lt;code object fun at 01523A38, file "C:/Users/João/Desktop/StackOverflow/so_hack.py", line 7&gt;
&lt;type 'ctypes.PyCFuncPtrType'&gt;
ctypes.py_object
__main__
&lt
