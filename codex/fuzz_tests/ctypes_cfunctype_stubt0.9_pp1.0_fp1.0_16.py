import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42 * 42

print ( "fun()",fun() )
</code>
The result is:
<code>fun() 1764
</code>
The problem is that ctypes can't return a C++ reference because it doesn't exist in the Python layer. Instead, you have the option to return a shared pointer that points to the C++ object, like you already did. 

