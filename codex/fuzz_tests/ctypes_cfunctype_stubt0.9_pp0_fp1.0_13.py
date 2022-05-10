import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    print("Hello world")
</code>
Then
<code>&gt;&gt;&gt; fun()()
Hello world
</code>

