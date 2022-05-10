import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

class square(ctypes.c_int):
    _fields_ = [("number", ctypes.c_int)]

p = square()
p.number = 30

myfunc = FUNTYPE(p.number)

print myfunc(1,1)
</code>
The exact error message is:
<code>Traceback (most recent call last):
  File "myclass.py", line 21, in &lt;module&gt;
    myfunc = FUNTYPE(p.number)
TypeError: must be convertible to a pointer
</code>


A:

You can't pass the result of <code>p.number</code> as a callable.  You need to pass in a function, or a pointer to a function.  You can create a function with the <code>ctypes</code> <code>CFUNCTYPE</code>.
<code>myfunc = CFUNCTYPE(ctypes.c_int, ctypes.c_int)(lambda x: x
