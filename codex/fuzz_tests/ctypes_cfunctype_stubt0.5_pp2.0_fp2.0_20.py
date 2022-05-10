import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

@FUNTYPE
def fun2():
    return "hello 2"

#fun = FUNTYPE(fun)

print fun()
print fun2()
</code>
The output is:
<code>hello
hello 2
</code>

