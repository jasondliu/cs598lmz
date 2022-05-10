import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def myfunc(a, b):
    print "myfunc", a, b
    return a + b

f = FUNTYPE(myfunc)

print f(1, 2)
</code>
This works fine, but I want to pass a pointer to a function in a dll. I can't figure out how to do it.
<code>import ctypes

dll = ctypes.WinDLL("mydll.dll")

FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

f = FUNTYPE(dll.myfunc)

print f(1, 2)
</code>
This gives me:
<code>Traceback (most recent call last):
  File "C:\Users\User\Desktop\test.py", line 12, in &lt;module&gt;
    f = FUNTYPE(dll.myfunc)
TypeError: function takes at most 2 arguments (3 given)

